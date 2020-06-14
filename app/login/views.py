from .models import User, Department, City
from .serializers import CitySerializer, DepartmentSerializer
from .serializers import UserSerializer, RegisterUserSerializer
from .serializers import UpdateUserSerializer
from rest_framework import viewsets, serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer, VehicleUpdateSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoints:
        /api/users
            GET - Returns a list of all users
        /api/users/<user_id>
            GET - Returns a single user identified by id or 404 if no match
        /api/users
            POST - Creates a new user
        /api/users/<user_id>
            PUT - Update user information
        /api/users/<user_id>/vehicles
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lockup_field = 'id'
    http_method_names = ['get', 'head', 'post', 'put']

    def create(self, request):
        """ User POST request
            /api/users POST - Creates a new user
        """
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            if data.get('password') != data.get('password2'):
                raise serializers.ValidationError({
                        'password': 'Passwords must match'
                        })
            department = Department.objects.get(id=data.get('department'))
            city = City.objects.get(id=data.get('city'))
            user = User.objects.create_user(data.get('first_name'),
                                            data.get('last_name'),
                                            data.get('type_id'),
                                            data.get('n_document'),
                                            department, city,
                                            data.get('picture'),
                                            data.get('email'),
                                            data.get('password'))
            r = {'response': 'User created successfully',
                 'user': UserSerializer(user).data}
            return Response(r, status=201)
        else:
            return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        """ User PUT request
            /api/users/<user_id> PUT - Update user information
        """
        serializer = UpdateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if request.data.get('first_name'):
                user.first_name = request.data.get('first_name')
            if request.data.get('last_name'):
                user.last_name = request.data.get('last_name')
            if request.data.get('department'):
                department = request.data.get('department')
                user.department = Department.objects.get(id=department)
            if request.data.get('city'):
                city = request.data.get('city')
                user.city = City.objects.get(id=city)
            user.picture = request.data.get('picture')
            if request.data.get('is_driver'):
                if request.data.get('is_driver') == 'True':
                    user.is_driver = True
                else:
                    user.is_driver = False
            user.save()
            r = {'response': 'Successfully updated',
                 'user': UserSerializer(user).data}
            return Response(r, status=200)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['GET'])
    def vehicles(self, request, pk):
        """
            /api/users/<user_id>/vehicles
                GET - Return list of vehicles of a user
        """
        user = self.get_object()
        vehicles = Vehicle.objects.filter(user=user)
        serializer = VehicleSerializer(vehicles, many=True)
        if len(serializer.data):
            return Response({'response': 'Succesful request',
                             'vehicles': serializer.data})
        else:
            return Response({'response': "User doesn't have\
                             any vehicle registered"}, status=404)

    @vehicles.mapping.post
    def create_vehicle(self, request, pk):
        """
            /api/users/<user_id>/vehicles
                POST - Create a new vehicle
        """
        user = self.get_object()
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            new_vehicle = Vehicle(plate=serializer.data['plate'],
                                  model=serializer.data['model'],
                                  color=serializer.data['color'],
                                  brand=serializer.data['brand'],
                                  user=user)
            new_vehicle.save()
            return Response({'response': 'Vehicle registered successfully',
                             'vehicle': VehicleSerializer(new_vehicle).data},
                            status=201)
        return Response(serializer.errors)

    @vehicles.mapping.put
    def update_vehicle(self, request, pk):
        """
            /api/users/<user_id>/vehicles/<vehicle_id>
                PUT - Update vehicle information
        """
        serializer = VehicleUpdateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                vehicle = Vehicle.objects.get(plate=request.data['plate'])
            except Exception as e:
                return Response({'response': "Vehicle with the associated\
                                              plate doesn't exists"},
                                status=404)
            if request.data.get('new_plate'):
                vehicle.plate = request.data.get('new_plate')
            if serializer.data.get('model'):
                vehicle.model = serializer.data.get('model')
            if serializer.data.get('color'):
                vehicle.color = serializer.data.get('color')
            if serializer.data.get('brand'):
                vehicle.brand = serializer.data.get('brand')
            vehicle.save()
            return Response({'response': 'Vehicle information \
                                          updated successfully',
                             'vehicle': VehicleSerializer(vehicle).data})
        return Response(serializer.errors)


class DepartmentViewSet(viewsets.ModelViewSet):
    """
        API endpoints:
        /api/departments:
            GET - Returns a list of all departments
        /api/departments/<id>:
            GET - Returns department filtered by id
        /api/departments/<id>/cities:
            GET - Returns list of cities filtered by department id
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lockup_field = 'id'
    http_method_names = ['get', 'head']

    @action(detail=True, methods=['GET'])
    def cities(self, request, pk):
        """
            GET REQUEST
            /api/departments/<id>/cities:
                GET - Returns list of cities filtered by department id
        """
        department = self.get_object()
        cities = City.objects.filter(department=department)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=200)


class CityViewSet(viewsets.ModelViewSet):
    """
        API endpoints:
        /api/cities: GET Return a list of all cities
    """
    http_method_names = ['get', 'head']
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CustomAuthToken(ObtainAuthToken):
    """
        API endpoints:
        /api/login:
            POST - Return token and user id if it success
                   Return "Wrong email or password" if it
                   fails
    """
    def post(self, request, *args, **kwargs):
        """ POST Request """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
            })
        else:
            raise serializers.\
                ValidationError(
                        {'Response error': 'Wrong email or password'})

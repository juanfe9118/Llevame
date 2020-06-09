from rest_framework.response import Response
from .models import User, Department, City
from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer
from rest_framework import viewsets, serializers
from .serializers import UserSerializer, RegisterUserSerializer, UpdateUserSerializer, DepartmentSerializer, CitySerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoints:
        /api/users GET - Returns a list of all users
        /api/users/<user_id> GET - Returns a single user identified by id or 404 if no match
        /api/users POST - Creates a new user
        /api/users/<user_id> PUT - Update user information
        /api/users/<user_id>/vehicles POST - Create a new vehicle
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
                raise serializers.ValidationError({'password': 'Passwords must match'})
            user = User.objects.create_user(data.get('first_name'), data.get('last_name'), data.get('type_id'), data.get('n_document'), data.get('department'), data.get('city'), data.get('picture'), data.get('email'), data.get('password'))
            r ={'response': 'User created successfully', 'user': UserSerializer(user).data}
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
            user.first_name = request.data.get('first_name')
            user.last_name = request.data.get('last_name')
            user.department = request.data.get('department')
            user.city = request.data.get('city')
            user.save()
            r = {'response': 'Successfully updated', 'user': UserSerializer(user).data}
            return Response(r, status=200)
        return Response(serializer.errors, status=400)

    
    @action(detail=True, methods=['GET'])
    def vehicles(self, request, pk):
        """
            GET REQUEST
            /api/users/<user_id>/vehicles GET - Return list of vehicles of a user
        """
        user = self.get_object()
        vehicles = Vehicle.objects.filter(user=user)
        serializer = VehicleSerializer(vehicles, many=True)
        if len(serializer.data):
            return Response({'response': 'Succesful request', 'vehicles': serializer.data, 'user': UserSerializer(user).data})
        else:
            return Response({'response': "User doesn't have any vehicle registered", 'user': UserSerializer(user).data}, status=404)


    @action(detail=True, methods=['POST'])
    def vehicles(self, request, pk):
        """
            POST REQUEST
            /api/users/<user_id>/vehicles POST - Create a new vehicle
        """
        user = self.get_object()
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            new_vehicle = Vehicle(plate=serializer.data['plate'], model=serializer.data['model'], color=serializer.data['color'], brand=serializer.data['brand'], user=user)
            new_vehicle.save()
            return Response({'response': 'Vehicle registered successfully', 'vehicle': VehicleSerializer(new_vehicle).data}, status=201)
        return Response(serializer.errors)

    
    @action(detail=True, methods=['PUT'])
    def vehicles(self, request, pk):
        """
            PUT REQUEST
            /api/users/<user_id>/vehicles/<vehicle_id> PUT - Update vehicle information
        """
        return Response('Developing')


class DepartmentViewSet(viewsets.ModelViewSet):
    """
        API endpoints:
        /api/departments: GET - Returns a list of all departments
        /api/departments/<id>: GET - Returns department filtered by id
        /api/departments/<id>/cities: GET - Returns list of cities filtered by department id
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lockup_field = 'id'
    http_method_names = ['get', 'head']

    @action(detail=True, methods=['GET'])
    def cities(self, request, pk):
        """
            GET REQUEST
            /api/departments/<id>/cities: GET - Returns list of cities filtered by department id
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

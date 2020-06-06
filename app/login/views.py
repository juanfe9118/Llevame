from rest_framework.response import Response
from .models import User, Department, City
from rest_framework import viewsets
from .serializers import UserSerializer, DepartmentSerializer, CitySerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoints:
        /api/users GET - Returns a list of all users
        /api/users/<user_id> GET - Returns a single user identified by id or 404 if no match
        /api/users POST - Creates a new user
        /api/users/<user_id> PUT - Update user information
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lockup_field = 'id'
    http_method_names = ['get', 'head', 'post', 'put']


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

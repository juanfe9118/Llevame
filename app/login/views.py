from rest_framework.response import Response
from .models import Department, City
from rest_framework import viewsets
from .serializers import DepartmentSerializer, CitySerializer
from rest_framework.decorators import action


class DepartmentViewSet(viewsets.ModelViewSet):
    """
        API endpoints:
        /departments: GET - Returns a list of all departments
        /departments/<id>: GET - Returns department filtered by id
        /departments/<id>/cities: GET - Returns list of cities filtered by department id
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lockup_field = 'id'
    http_method_names = ['get', 'head']

    @action(detail=True, methods=['GET'])
    def cities(self, request, pk):
        print(request)
        department = self.get_object()
        cities = City.objects.filter(department=department)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=200)


class CityViewSet(viewsets.ModelViewSet):
    """
        API endpoints:
        /cities: GET Return a list of all cities
    """
    http_method_names = ['get', 'head']
    queryset = City.objects.all()
    serializer_class = CitySerializer

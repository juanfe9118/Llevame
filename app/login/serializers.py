from .models import Department, City
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    """
        DepartmentSerializer
    """
    class Meta:
        model = Department
        fields = ['id', 'name', 'code']

class CitySerializer(serializers.ModelSerializer):
    """
        City Serializer
    """
    class Meta:
        model = City
        fields = ['id', 'department', 'code', 'name']

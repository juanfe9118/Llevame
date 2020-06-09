from .models import Vehicle
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    """ Vehicle Serializer """
    class Meta:
        model = Vehicle
        fields = ['plate', 'model', 'color', 'brand', 'user']
        extra_kwargs = {'user': {'read_only': True}}
from .models import Vehicle
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    """ Vehicle Serializer """
    class Meta:
        model = Vehicle
        fields = ['plate', 'model', 'color', 'brand', 'user']
        extra_kwargs = {'user': {'read_only': True}}


class VehicleUpdateSerializer(serializers.ModelSerializer):
    """ Vehicle Update Serializer """
    new_plate = serializers.CharField(style={'input_type': 'text'},
                                      max_length=6, write_only=True,
                                      required=False)

    class Meta:
        model = Vehicle
        fields = ['plate', 'new_plate', 'model', 'color', 'brand', 'user']
        extra_kwargs = {'user': {'read_only': True},
                        'plate': {'validators': []},
                        'model': {'required': False},
                        'color': {'required': False},
                        'brand': {'required': False}
                        }

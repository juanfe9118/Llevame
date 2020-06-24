from .models import User, Department, City, Feedback
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer """
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'type_id', 'n_document',
                  'department', 'city',
                  'picture', 'email', 'is_driver', 'date_joined']


class RegisterUserSerializer(serializers.ModelSerializer):
    """ Register Serializer """
    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'type_id', 'n_document',
                  'department', 'city', 'picture', 'email',
                  'date_joined', 'password', 'password2']


class UpdateUserSerializer(serializers.ModelSerializer):
    """ Update Serializer """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'department', 'city',
                  'picture', 'is_driver', 'date_joined']
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'department': {'required': False},
            'city': {'required': False},
            'picture': {'required': False}
        }


class DepartmentSerializer(serializers.ModelSerializer):
    """ Department Serializer """
    class Meta:
        model = Department
        fields = ['id', 'name', 'code']


class CitySerializer(serializers.ModelSerializer):
    """ City Serializer """
    class Meta:
        model = City
        fields = ['id', 'department', 'code', 'name']

class FeedbackSerializer(serializers.ModelSerializer):
    """
    Converts Message model data to native python data types
    """
    class Meta:
        model = Feedback
        fields = ['id', 'recipient', 'sender', 'score', 'comment']

class FeedbackSerializerList(serializers.ModelSerializer):
    """
    Handles GET verb returning a list of feedbacks using the model data
    """
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)
    class Meta:
        model = Feedback
        fields = ['id', 'recipient', 'sender', 'score', 'comment', 'pub_date']

class UpdateFeedbackSerializer(serializers.ModelSerializer):
    """
    Handles PUT verb updating a feedback using the model data
    """
    class Meta:
        model = Feedback
        fields = ['id', 'recipient', 'sender', 'score', 'comment']
        read_only_fields = ['id', 'recipient', 'sender']


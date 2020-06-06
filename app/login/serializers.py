from .models import User, Department, City
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer """
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['first_name', 'last_name', 'type_id', 'n_document', 'department', 'city', 'email', 'date_joined', 'password']

    def create(self, data):
        """ User POST request
            /api/users POST - Creates a new user
        """
        user = User.objects.create_user(data['first_name'], data['last_name'], data['type_id'], data['n_document'], data['department'], data['city'], data['email'], data['password'])
        return user

    def update(self, user, data):
        """ User PUT request
            /api/users/<user_id> PUT - Update user information
        """
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.type_id = data['type_id']
        user.n_document = data['n_document']
        user.department = data['department']
        user.city = data['city']
        user.save()
        return user


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

"""
Converts data to native python data types
"""
from .models import Chat, Message
from login.models import User
from login.serializers import UserSerializer
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    """
    Converts Message model data to native python data types
    """

    class Meta:
        model = Message
        fields = ['id', 'user', 'chat', 'pub_date', 'content']

class UpdateMessageSerializer(serializers.ModelSerializer):
    """
    Handles PUT verb in message serialization
    """
    class Meta:
        model = Message
        fields = ['content']


class ChatSerializer(serializers.ModelSerializer):
    """
    Converts Chat model data to native python data types
    """
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'token', 'users', 'messages']

"""
Converts data to native python data types
"""
from .models import Chat, Message
from ..login.models import User
from ..login.serializers import UserSerializer
from rest_framework import serializers


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    """
    Converts Message model data to native python data types
    """

    class Meta:
        model = Message
        fields = ['id', 'chat', 'pub_date', 'content']

class ChatSerializer(serializers.HyperlinkedModelSerializer):
    """
    Converts Chat model data to native python data types
    """

    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Chat
        fields = ['id', 'token', 'users', 'messages']

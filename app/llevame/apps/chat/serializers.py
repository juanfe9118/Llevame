from llevame.apps.chat.models import chats, messages
from rest_framework import serializers


class messages_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = messages
        fields = ['url', 'pub_date', 'content', 'chat']

class chat_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = chats
        fields = ['url', 'token']

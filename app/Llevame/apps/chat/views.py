from llevame.apps.chat.models import chats, messages
from rest_framework import viewsets
from llevame.apps.chat.serializers import chat_serializer, messages_serializer


class message_view_set(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = messages.objects.all().order_by('-date_joined')
    serializer_class = messages_serializer

class chat_view_set(viewsets.ModelViewSet):
    """
    API endpoint that allows chats to be viewed or edited.
    """
    queryset = chats.objects.all()
    serializer_class = chat_serializer

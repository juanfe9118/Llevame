from .models import chats, messages
from .serializers import chat_serializer, messages_serializer
from rest_framework import viewsets

class chats_view_set(viewsets.ModelViewSet):
    """
    API endpoint that allows chats to be viewd or edited.
    """

    queryset = chats.objects.all().order_by('-date_joined')
    serializer_class = chat_serializer


class messages_view_set(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewd or edited.
    """

    queryset = messages.objects.all().order_by('-date_joined')
    serializer_class = messages_serializer

from .models import chats, messages
from rest_framework import viewsets
from .serializers import chat_serializer, messages_serializer


class message_view_set(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = messages.objects.all().order_by('pub_date')
    serializer_class = messages_serializer

class chat_view_set(viewsets.ModelViewSet):
    """
    API endpoint that allows chats to be viewed or edited.
    """
    queryset = chats.objects.all()
    serializer_class = chat_serializer

from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer, UpdateMessageSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Message.objects.all().order_by('pub_date')
    # serializer_class = MessageSerializer

    def get_serializer_class(self):
        if (self.request.method == "PUT"):
            return UpdateMessageSerializer
        else:
            return MessageSerializer


class ChatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows chats to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['GET'], detail=True)
    def messages(self, request, pk=None):
        """
        /api/chats/<id>/messages
        GET - Returns a list of messages associated with the chat
        """
        chat = self.get_object()
        messages = Message.objects.filter(chat=chat)
        context = {
        'request': request
        }
        serializer = MessageSerializer(messages, many=True, context=context)
        return Response(serializer.data)


    queryset = Chat.objects.all().order_by('id')
    serializer_class = ChatSerializer

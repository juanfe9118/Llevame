"""
    Defines the data models for the chat app
"""
from django.db import models
from django.utils import timezone
from login.models import User, Token


class Chat(models.Model):
    """
        Defines the chats data model
    """

    token = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    users = models.ManyToManyField(User, related_name='users')

    def __str__(self):
        """
            String representation of object
        """

        return self.token

class Message(models.Model):
    """
        Defines the messages data model
    """

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    pub_date = models.DateTimeField('date published', default=timezone.now)
    content = models.CharField(max_length=200)

    def __str__(self):
        """
            String representation of object
        """

        return '{} - {}'.format(self.pub_date, self.content)

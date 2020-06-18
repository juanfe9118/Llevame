"""
    Defines the data models for the chat app
"""
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from login.models import User
from uuid import uuid4


class Chat(models.Model):
    """
        Defines the chats data model
    """

    token = models.UUIDField(default=uuid4, editable=False)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    users = models.ManyToManyField(User, related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        """
            String representation of object
        """

        return '{} - {}'.format(self.id, self.token)

class Message(models.Model):
    """
        Defines the messages data model
    """

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    pub_date = models.DateTimeField('date published', default=timezone.now)
    content = models.CharField(max_length=200)

    def __str__(self):
        """
            String representation of object
        """

        return '{} - {}'.format(self.pub_date, self.content)

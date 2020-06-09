'''
    Defines the data models for the chat app
'''
from django.db import models


class chats(models.Model):
    '''
        Defines the chats data model
    '''

    token = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        '''
            String representation of object
        '''

        return self.token

class messages(models.Model):
    '''
        Defines the messages data model
    '''

    chat = models.ForeignKey(chats, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    content = models.CharField(max_length=200)

    def __str__(self):
        '''
            String representation of object
        '''

        return '{} - {}'.format(self.pub_date, self.content)

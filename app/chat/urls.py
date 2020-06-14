"""
Define the routes associated with chats api
"""
from . import views
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)
router.register(r'chats', views.ChatViewSet)

urlpatterns = path = [
    path('', include(router.urls)),
]

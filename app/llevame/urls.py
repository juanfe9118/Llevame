"""llevame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .apps.chat import views


router = routers.DefaultRouter()
router.register(r'messages', views.message_view_set)
router.register(r'chats', views.chat_view_set)

urlpatterns = [
    path('', include(router.urls)),
    path('api-chat/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

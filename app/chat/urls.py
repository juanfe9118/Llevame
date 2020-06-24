from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'chats', views.ChatViewSet)
router.register(r'messages', views.MessageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# POST request to /api/login must have username in the request
# and this must be email
# Is like django login works, but we have set email as username

urlpatterns = [
    path('', include(router.urls)),
]

from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.urls import include, path
from django.views.static import serve
from rest_framework import routers
from login import views as login_views
from chat import views as chat_views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', login_views.UserViewSet)
router.register(r'departments', login_views.DepartmentViewSet)
router.register(r'cities', login_views.CityViewSet)
router.register(r'chats', chat_views.ChatViewSet)
router.register(r'messages', chat_views.MessageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# POST request to /api/login must have username in the request
# and this must be email
# Is like django login works, but we have set email as username

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'login/', login_views.CustomAuthToken.as_view())
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]

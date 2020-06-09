from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'cities', views.CityViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# POST request to /api/login must have username in the request and this must be email
# Is like django login works, but we have set email as username
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', obtain_auth_token, name='login')
]
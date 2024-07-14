from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet

app_name = 'users'

router = SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

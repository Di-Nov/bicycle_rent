from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]

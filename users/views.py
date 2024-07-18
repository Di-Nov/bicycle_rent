from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import viewsets

from .models import CustomUser
from api.v1.serializers import UserSerializer


# @extend_schema(
#     parameters=[
#         OpenApiParameter(name='artist', description='Filter by artist', required=False, type=str)
#     ]
# )
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

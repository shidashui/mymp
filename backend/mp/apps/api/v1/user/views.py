from rest_framework import viewsets

from api.v1.user.serializers import SchoolSerializers, UserSerializers
from base.models import School, User


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializers
    queryset = School.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    lookup_field = 'token'

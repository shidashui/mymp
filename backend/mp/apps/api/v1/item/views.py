from rest_framework import viewsets

from api.v1.item.serializers import SchoolSerializers
from base.models import School


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializers
    queryset = School.objects.all()
from rest_framework import serializers

from base.models import School


class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
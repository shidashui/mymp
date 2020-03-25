from rest_framework import serializers

from base.models import School, User


class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("open_id", "session_key", "token", "auth_img", "role_code")
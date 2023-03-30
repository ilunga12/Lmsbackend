from rest_framework import serializers

from backapp.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'password', 'mobile_no', 'address']
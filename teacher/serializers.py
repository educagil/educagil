from rest_framework.serializers import ModelSerializer

from teacher.models import Teacher


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'email', 'first_name', 'last_name', 'user_type']

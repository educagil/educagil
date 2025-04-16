from rest_framework import serializers

from teacher.models import Teacher
from user.serializers import UserSerializer


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'user']

    @classmethod
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(user_data)  # Cria o User
        # Cria o Teacher
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher


from rest_framework import viewsets

from teacher.models import Teacher
from teacher.serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

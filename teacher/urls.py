from django.urls import include, path
from rest_framework.routers import DefaultRouter

from teacher.viewsets import TeacherViewSet

router = DefaultRouter(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

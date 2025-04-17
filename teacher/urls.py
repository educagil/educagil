from django.urls import include, path
from rest_framework.routers import DefaultRouter

from teacher.viewsets import TeacherViewSet

router = DefaultRouter()
router.register(r'', TeacherViewSet, basename='teacher')


urlpatterns = [
    # path('', include(router.urls)),
    path(
        'create_user/',
        TeacherViewSet.as_view({'post': 'create'}),
        name='teacher_create_user'
    )
]

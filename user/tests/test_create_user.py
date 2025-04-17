import pytest
from django.urls import reverse
from rest_framework import status

from teacher.models import Teacher


@pytest.mark.django_db
def test_user_create(client):
    url = reverse('teacher_create_user')
    data = {
        'first_name': 'Test',
        'last_name': 'Test',
        'email': 'test@test.com',
        'password': 'test',
        'user_type': 'T'
    }

    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Teacher.objects.count == 1
    teacher = Teacher.objects.first()
    assert teacher.email == 'test@test.com'

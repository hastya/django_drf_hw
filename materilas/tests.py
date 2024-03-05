from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from materilas.models import Course, CourseSubscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        # Создание пользователя
        self.client = APIClient()
        self.user = User.objects.create(
            email="test@user1.com",
            is_superuser=True,
            is_staff=True
        )
        self.client.force_authenticate(user=self.user)

        # Создание курса
        self.course = Course.objects.create(
            name='test',
            description='first course',
            owner=self.user
        )

    def test_get_lesson_authenticated(self):
        """ Получение курса уроков авторизованным пользователем."""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('materilas:lesson-list')
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class CourseSubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        # Создание пользователя
        self.client = APIClient()
        self.user = User.objects.create(
            email="test@user2.com",
            is_superuser=True,
            is_staff=True
        )
        self.client.force_authenticate(user=self.user)

        # Создание курса
        Course.objects.create(name='test2')

    def test_subscribe_to_course(self):
        """Тест проверки подписки на курс"""

        data = {
            "course_id": 1,
            "user": 1
        }

        response = self.client.post(
            '/courses/subscription/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

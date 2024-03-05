from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from materilas.models import Course, CourseSubscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        # Создание пользователя
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
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
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

        # Создание курса
        self.course = Course.objects.create(
            name="test_course",
            description='second course',
            owner=self.user
        )

        # Создаем подписки
        self.subscribe = CourseSubscription.objects.create(
            user=self.user,
            course=self.course,
        )

    def test_subscribe_to_course(self):
        """Тест проверки подписки на курс"""

        data = {
            "course_id": 1,
            "user": 1
        }

        response = self.client.post(
            reverse('materilas:course-subscription'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

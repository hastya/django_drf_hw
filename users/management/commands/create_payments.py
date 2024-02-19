from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils import timezone

from materilas.models import Course, Lesson
from users.models import Payments

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Создание тестового пользователя
        user = User.objects.create(username='AnPo', first_name='Anna', last_name='Popova', email='Anna@popova.com')

        # Создание тестового курса
        course = Course.objects.create(name='backend', description='this is the backend course')

        # Создание тестового урока
        lesson = Lesson.objects.create(name='lesson_Python', description='this is the lesson_Python', course=course)

        # Создание тестовой оплаты
        payment = Payments.objects.create(
            user=user,
            date_of_payment=timezone.now(),
            paid_course=course,
            paid_lesson=lesson,
            payment_amount=222.33,
            payment_method='transfer'
        )

        self.stdout.write(self.style.SUCCESS('Successfully created sample payments'))

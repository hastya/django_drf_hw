from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from materilas.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):

    MEMBER = 'member', _('member'),
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name='фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=50, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Payments(models.Model):

    PAYMENT_CHOICES = [
        ('transfer', 'transfer to account'),
        ('cash', 'cash'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='payment')
    date_of_payment = models.DateField(verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный курс', related_name='course')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный урок', related_name='lesson')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_CHOICES, verbose_name='способ оплаты')

    payment_url = models.URLField(max_length=400, **NULLABLE, verbose_name='ссылка на оплату')
    payment_id = models.CharField(max_length=100, **NULLABLE, verbose_name='идентификатор платежа')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

    def __str__(self):
        return f'{self.user} оплата {self.date_of_payment}'

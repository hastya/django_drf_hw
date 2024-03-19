from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

from users.models import User


# @shared_task
# def check_user_activity(user_id):
#     user = User.objects.get(id=user_id)
#     if user.last_login < timezone.now() - timezone.timedelta(days=30):
#         user.is_active = False
#         user.save()

@shared_task
def check_user_activity():
    user = get_user_model()
    now = timezone.now()
    month_ago = now - relativedelta(months=1)
    user_is_active = User.objects.filter(last_login__lt=month_ago, is_active=True)
    user_is_active.update(is_active=False)
    print(f'Deactivated {user_is_active.count()} users')

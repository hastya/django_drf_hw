from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@test.com',
            first_name='Test',
            last_name='Test',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('123qwe456rty')
        user.save()

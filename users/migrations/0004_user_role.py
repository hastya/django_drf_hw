# Generated by Django 4.2.3 on 2024-02-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'member'), ('moderator', 'moderator')], default='member', max_length=9),
        ),
    ]

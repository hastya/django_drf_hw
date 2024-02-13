from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined']

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated

from materilas.permissions import IsOwner, IsModerator
from users.models import User, Payments
from users.serializers import UserSerializer, PaymentSerializer
from users.services import create_stripe_price, create_stripe_session


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        password = validated_data.get('password')
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class PaymentListApiView(generics.ListAPIView):
    """ Список платежей """
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('date_of_payment',)
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class PaymentCreateView(generics.CreateAPIView):
    """ Cоздание нового платежа """
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        course = serializer.validated_data.get('paid_course')
        if not course:
            raise serializers.ValidationError('Укажите курс')
        payment = serializer.save()
        stripe_price_id = create_stripe_price(payment)
        payment.payment_url, payment.payment_id = (
            create_stripe_session(stripe_price_id)
        )
        payment.save()


class PaymentDetailView(generics.RetrieveAPIView):
    """ Просмотр информации по платежу """
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all
    permission_classes = [IsAuthenticated, IsOwner]


class PaymentUpdateView(generics.UpdateAPIView):
    """ Обновление данных по платежу """
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all
    permission_classes = [IsAuthenticated, IsOwner]


class PaymentDestroyView(generics.DestroyAPIView):
    """ Удаление платежа """
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all
    permission_classes = [IsAuthenticated, IsOwner]

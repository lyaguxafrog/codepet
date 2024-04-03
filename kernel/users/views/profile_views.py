# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework import generics
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from users.serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        summary='Создать пользователя',
        description='Создать пользователя и профиль',
        request=UserSerializer,
        responses={
            status.HTTP_201_CREATED: 'Пользователь создан',
            status.HTTP_400_BAD_REQUEST: 'Неверные данные',
            status.HTTP_500_INTERNAL_SERVER_ERROR: 'Ошибка при создании пользователя'
        }
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

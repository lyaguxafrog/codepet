# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User

from users.services.create_profile import create_profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'repeat_password',
            'first_name',
            'last_name',
            'patronymic'
            ]

        extra_kwargs = {
            'password':
                {'write_only': True},

            'repeat_password':
                {'write_only': True}
        }

    def create(self, validated_data):
        # Извлекаем пароль из валидированных данных
        password = validated_data.pop('password', None)
        repeat_password = validated_data.pop('repeat_password', None)

        # Создаем пользователя и профиль
        user_profile = create_profile(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password,
            repeat_password=repeat_password,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            patronymic=validated_data.get('patronymic', None)
        )
        return user_profile.user

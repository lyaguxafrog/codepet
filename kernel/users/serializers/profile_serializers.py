# -*- coding: utf-8 -*-

from rest_framework import serializers

from users.services.create_profile import create_profile

class UserSerializer(serializers.Serializer):
    """
    Создание пользователя
    """
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    patronymic = serializers.CharField(max_length=100, required=False)


    def validate(self, data):
        if data.get('password') != data.get('repeat_password'):
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def create(self, validated_data):
        # Извлекаем пароль из валидированных данных
        password = validated_data.pop('password', None)
        # Создаем пользователя и профиль
        user_profile = create_profile(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password,
            repeat_password=password,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            patronymic=validated_data.get('patronymic', None)
        )

        return user_profile.user

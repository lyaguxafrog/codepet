# -*- coding: utf-8 -*-

from typing import Optional

from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.db.transaction import atomic
from django.contrib.auth.models import User

from users.models import UserProfile

validate_username = ASCIIUsernameValidator()


@atomic
def create_profile(
        username: str,
        email: str,
        password: str,
        repeat_password: str,
        first_name: str,
        last_name: str,
        patronymic: Optional[str]
    ) -> UserProfile:
    """
    Сервис для создания профиля пользователя

    :param username: Имя пользователя, проходит `ASCIIUsernameValidator`
    :param email: E-mail пользователя, проходит `validate_email`
    :param password: Пароль пользователя, проходит `validate_password`
    :param repeat_password: Повторный ввод пароля, сравнивается с `password`
    :param first_name: Имя
    :param last_name: Фамилия
    :param patronymic: Отчество, необязательный параметр
    """

    # проверки введенных данных на валидность
    if repeat_password != password:
        raise Exception('Пароли не совпадают')

    validate_password(password=password)
    validate_email(email)
    validate_username(username)

    if User.objects.filter(username=username).exists():
        raise Exception('Пользователь с таким именем уже существует')

    if User.objects.filter(email=email).exists():
        raise Exception('Email уже используется')

    # cоздаем django-пользователя
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )

    # создаем профиль
    user_profile = UserProfile.objects.create(
        user=user,
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,
    )

    return user_profile

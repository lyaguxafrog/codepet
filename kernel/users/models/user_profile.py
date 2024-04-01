# -*- code: utf-8 -*-

from django.db import models


class UserProfile(models.Model):
    """
    Модель профиля пользователя
    """

    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    first_name = models.CharField(
        max_length=256,
        verbose_name='Имя'
    )

    last_name = models.CharField(
        max_length=256,
        verbose_name='Фамилия'
    )

    patronymic = models.CharField(
        max_length=256,
        null=True, blank=True,
        verbose_name='Отчество, при наличии'
    )

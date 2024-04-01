# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models

from users.models import UserProfile

class Collect(models.Model):
    """
    Модель сбора средств
    """

    collect_owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Владелец сбора'
    )

    collect_name = models.CharField(
        max_length=256,
        null=False,
        verbose_name='Название'
    )

    reason = models.CharField(
        max_length=256,
        null=False,
        verbose_name='Повод'
    )

    description = models.TextField(
        verbose_name='Описание сбора'
    )

    collect_goal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Цель сбора'
    )

    collected_sum = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0,
        verbose_name='Сколько уже собрали'
    )

    person_count = models.IntegerField(
        null=False,
        default=1,
        verbose_name='Сколько человек участвует в сборе'
    )

    cover = models.ImageField(
        blank=True, null=True,
        verbose_name="Обложка"
    )

    end_date = models.DateTimeField(
        verbose_name="Дата конца сбора средств",
        null=True, blank=True
    )

    status = models.BooleanField(
        default=True,
        verbose_name="Статус сбора"
    )


class DonatersList(models.Model):
    """
    Модель списка доноров
    """

    donate_to = models.ForeignKey(
        Collect,
        on_delete=models.CASCADE,
        verbose_name='Куда донатил'
    )

    doneter = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Донатер'
    )

    donate_sum = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        verbose_name='Сумма пожертвования'
    )

    donate_date = models.DateTimeField(
        default=datetime.now,
        verbose_name='Дата пожертвования'
    )

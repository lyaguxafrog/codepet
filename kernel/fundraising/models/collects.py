# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models

from users.models import UserProfile

class Collect(models.Model):
    """
    Модель сбора средств

    * `collect_owner` - ссылка на `users.UserProfile`
    * `collect_name` - название сбора | varchar(256), not null
    * `reason` - причина/повод сбора, выпадающий список | varchar(256), not null
    * `description` - описание сбора | text
    * `collect_goal` - Цель сбора(сумма) | numeric 10/2, default:0, not null
    * `collected_sum` - Сколько уже собрали | numeric 10/2, default:0, not null
    * `person_count` - Кол-во донатеров | integer, default:0, not null
    * `cover` - Обложка сбора | varchar(100)
    * `end_date` - Дата завершения сбора | timestamp
    * `status` - Статус активности сбора | boolean, default:True
    """

    collect_owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Владелец сбора'
    )

    collect_name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    reason = models.CharField(
        max_length=256,
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
        default=0,
        verbose_name='Сколько уже собрали'
    )

    person_count = models.IntegerField(
        default=0,
        verbose_name='Сколько человек участвует в сборе'
    )

    cover = models.ImageField(
        blank=True, null=True,
        verbose_name="Обложка"
    )

    create_date = models.DateTimeField(
        default=datetime.now,
        verbose_name="Дата создания сбора"
    )

    end_date = models.DateField(
        null=True, blank=True,
        verbose_name="дата конца сбора средств",
    )

    status = models.BooleanField(
        default=True,
        verbose_name="Статус сбора",
        help_text="True - сбор активен, False - нет"
    )

    contributors = models.JSONField(
        default=list,
        blank=True,
        verbose_name='Список идентификаторов донатеров'
    )

    def deactivate(self):
        self.status = False
        self.save()

    def __str__(self):
        return self.collect_name

    class Meta:
        verbose_name='Сбор'
        verbose_name_plural='Сборы'

# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models

from fundraising.models import Collect
from users.models import UserProfile


class Payment(models.Model):
    """
    Модель платежа

    * `pay_to` - Ссылка на `fundraising.Collect`
    * `payer` - Ссылка на `users.UserProfile`
    * `sum` - Сумма доната | numeric 10/2, not null
    * `date` - Дата доната | timestamp, default:now, not null
    """

    pay_to = models.ForeignKey(
        Collect,
        on_delete=models.CASCADE,
        verbose_name='Ключ на `collect`'
    )

    payer = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Ключ на `user_profile`'
    )

    sum = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        verbose_name='Сумма пожертвования'
    )

    date = models.DateTimeField(
        default=datetime.now,
        verbose_name='Дата пожертвования'
    )

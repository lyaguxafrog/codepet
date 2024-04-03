# -*- coding: utf-8 -*-

from typing import Union
from decimal import Decimal

from django.db.transaction import atomic

from fundraising.models import Collect, Payment
from users.models import UserProfile


@atomic
def pay(
        pay_to: int,
        payer: int,
        sum: float
    ) -> Union[Payment, Exception]:
    """
    Функция платежа

    :param pay_to: Идентификатор объекта `Collect` куда идет платеж
    :param payer: Идентификатор объекта `UserProfile`, тот кто платит
    :param sum: Сумма платежа

    :return: Созданный платеж или ошибка
    """


    pay_to_obj = Collect.objects.get(id=pay_to)
    payer_obj = UserProfile.objects.get(id=payer)

    if not pay_to_obj.status:
        raise Exception("Сбор закрыт")

    if not Payment.objects.filter(pay_to=pay_to_obj, payer=payer_obj).exists():
        pay_to_obj.collected_sum += Decimal(sum)
        pay_to_obj.person_count += 1
        pay_to_obj.save()


    payment = Payment.objects.create(
        pay_to=pay_to_obj,
        payer=payer_obj,
        sum=sum
    )

    return payment

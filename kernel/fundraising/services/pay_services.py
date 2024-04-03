# -*- coding: utf-8 -*-

from typing import Union

from django.db.transaction import atomic

from fundraising.models import Collect, Payment
from users.models import UserProfile


@atomic
def pay(
        pay_to: Collect,
        payer: UserProfile,
        sum: float
    ) -> Union[Payment, Exception]:
    """
    Функция платежа

    :param pay_to: Объект `Collect` куда идет платеж
    :param payer: Объект `UserProfile`, тот кто платит
    :param sum: Сумма платежа

    :return: Созданный платеж или ошибка
    """

    if pay_to.status == False:
        raise Exception("Сбор закрыт")

    if not Payment.objects.filter(pay_to=pay_to, payer=payer).exists():
        pay_to.sum += sum
        pay_to.person_count += 1
        pay_to.save()

    payment = Payment.objects.create(
        pay_to=pay_to,
        payer=payer,
        sum=sum
    )

    return payment

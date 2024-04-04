# -*- coding: utf-8 -*-

from typing import Union
from decimal import Decimal
from django.db.transaction import atomic

from fundraising.models import Collect, Payment
from users.models import UserProfile


@atomic
def update_payment(
        payment: Payment,
        sum: float
    ) -> Union[Payment, Exception]:
    """
    Обновляет существующий платеж, увеличивая сумму в связанном объекте Collect и увеличивая person_count, если пользователь еще не был учтен.

    :param payment: Объект Payment, который нужно обновить
    :param sum: Сумма платежа

    :return: Обновленный платеж или ошибка
    """

    if sum <= 0:
        raise Exception("Сумма платежа должна быть положительной")


    payment.sum += Decimal(sum)
    payment.save()


    collect_obj = payment.pay_to
    collect_obj.collected_sum += Decimal(sum)


    if payment.payer.id not in collect_obj.contributors:
        collect_obj.person_count += 1

        collect_obj.contributors.append(payment.payer.id)

    collect_obj.save()

    return payment

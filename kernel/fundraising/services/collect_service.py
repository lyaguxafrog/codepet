# -*- coding: utf-8 -*-

from django.db.transaction import atomic

from users.models import UserProfile
from fundraising.models import Collect

@atomic
def stop_collect(
        collect: Collect,
        owner: UserProfile
    ) -> Collect:
    """
    Функция для остановки сбора.

    :param collect: Экземпляр сбора, который нужно остановить.
    :param owner: Владелец сбора, выполняющий операцию.
    :return: Обновленный экземпляр сбора с измененным статусом.
    """

    # Проверяем, что владелец сбора является тем, кто пытается остановить сбор
    if collect.collect_owner != owner:
        raise Exception('Только владелец сбора может остановить его.')

    # Изменяем статус сбора на False
    collect.status = False
    collect.save()

    return collect

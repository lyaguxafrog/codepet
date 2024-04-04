# -*- coding: utf-8 -*-

import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from django_celery_beat.models import PeriodicTask, IntervalSchedule

from fundraising.models import Collect


@receiver(post_save, sender=Collect)
def close_collect_if_goal_reached(sender, instance, **kwargs):
    """
    Сигнал, который закрывает сбор,
    если сумма сбора достигла или превысила цель.
    """
    # Проверяем, что сигнал не вызван из-за изменения статуса
    if 'update_fields' in kwargs and kwargs['update_fields'] is not None and 'status' in kwargs['update_fields']:
        return

    if instance.collected_sum >= instance.collect_goal:
        instance.status = False
        instance.save(update_fields=['status'])


@receiver(post_save, sender=Collect)
def create_deactivate_collect_task(sender, instance, created, **kwargs):
    if created:
        # Создаем новый график для задачи
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.DAYS,
        )
        # Создаем задачу, которая будет выполняться по этому графику
        PeriodicTask.objects.create(
            interval=schedule,
            name=f'Deactivate Collect {instance.id}',
            task='fundraising.fundraising.tasks.check_and_deactivate_collect',
            args=json.dumps([instance.id]),
            start_time=timezone.now(),
        )

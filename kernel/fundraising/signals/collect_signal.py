# -*- coding: utf-8 -*-

from django.db.models.signals import post_save
from django.dispatch import receiver

from fundraising.models import Collect

@receiver(post_save, sender=Collect)
def close_collect_if_goal_reached(sender, instance, **kwargs):
    """
    Сигнал, который закрывает сбор,
    если сумма сбора достигла или превысила цель.
    """

    if instance.collected_sum >= instance.collect_goal:
        instance.status = False
        instance.save()

# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.utils import timezone

from fundraising.models import Collect

@shared_task
def check_and_deactivate_collect(collect_id):
    collect = Collect.objects.get(id=collect_id)
    if collect.end_date and collect.end_date <= timezone.now():
        collect.status = False
        collect.save()

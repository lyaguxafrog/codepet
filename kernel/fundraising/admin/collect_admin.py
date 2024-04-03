# -*- coding: utf-8 -*-

from django.contrib import admin

from fundraising.models import Collect


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    fields = [
        'collect_owner',
        'collect_name',
        'cover',
        'description',
        'reason',
        'collect_goal',
        'collected_sum',
        'person_count',
        'create_date',
        'end_date',
        'status',
    ]

    readonly_fields = [
        'collected_sum',
        'person_count',
        'create_date'
    ]

    list_display = [
        'collect_name',
        'collect_owner',
        'collect_goal',
        'collected_sum',
        'create_date',
    ]

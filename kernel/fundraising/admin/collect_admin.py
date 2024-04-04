# -*- coding: utf-8 -*-

from django.contrib import admin
from django.http import HttpRequest

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
        'contributors',
        'create_date',
        'end_date',
        'status',
    ]

    readonly_fields = [field for field in fields if field != 'status']

    list_display = [
        'collect_name',
        'collect_owner',
        'collect_goal',
        'collected_sum',
        'create_date',
        'status',
    ]

    list_filter = [
        'status'
    ]

    def open_collect(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "Сборы успешно открыты.")
    open_collect.short_description = "Открыть сбор"

    def close_collect(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "Сборы успешно закрыты.")
    close_collect.short_description = "Закрыть сбор"

    actions = [open_collect, close_collect]




    def has_delete_permission(
        self, request: HttpRequest, obj: Collect = None,
    ) -> bool:
        return False

    def has_add_permission(self, requst: HttpRequest) -> bool:
        return False

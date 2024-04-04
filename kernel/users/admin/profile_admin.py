# -*- coding: utf-8 -*-

from django.contrib import admin
from django.http import HttpRequest

from users.models import UserProfile


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    fields = [
        'user',
        'first_name',
        'last_name',
        'patronymic',
        'create_date',
    ]

    readonly_fields = fields

    list_display = [
        'user',
        'first_name',
        'last_name',
        'create_date',
    ]

    search_fields = [
        'user',
        'first_name',
        'last_name',
        'patronymic',
        'create_date',
    ]


    def has_delete_permission(
        self, request: HttpRequest, obj: UserProfile = None,
    ) -> bool:
        return False

    def has_add_permission(self, requst: HttpRequest) -> bool:
        return False

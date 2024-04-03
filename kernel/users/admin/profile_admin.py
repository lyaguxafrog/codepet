# -*- coding: utf-8 -*-

from django.contrib import admin

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

    readonly_fields = [
        'user',
        'create_date',
    ]

    list_display = [
        'user',
        'first_name',
        'last_name',
        'create_date',
    ]

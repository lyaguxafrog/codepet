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
    ]

    readonly_fields = [
        'user',
    ]

    list_display = [
        'user',
    ]

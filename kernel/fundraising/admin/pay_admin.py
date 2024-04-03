# -*- coding: utf-8 -*-

from django.contrib import admin

from fundraising.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fields = [
        'pay_to',
        'payer',
        'sum',
        'date'
    ]

    readonly_fields = [
        'date',
    ]

    list_display = [
        'pay_to',
        'payer',
        'sum',
        'date'
    ]

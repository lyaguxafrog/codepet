# -*- coding: utf-8 -*-

from django.contrib import admin
from django.http import HttpRequest

from fundraising.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fields = [
        'pay_to',
        'payer',
        'sum',
        'date'
    ]

    readonly_fields = fields

    list_display = [
        'pay_to',
        'payer',
        'sum',
        'date'
    ]

    def has_delete_permission(
        self, request: HttpRequest, obj: Payment = None,
    ) -> bool:
        return False

    def has_add_permission(self, requst: HttpRequest) -> bool:
        return False

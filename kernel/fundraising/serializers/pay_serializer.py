# -*- coding: utf-8 -*-

from rest_framework import serializers

from fundraising.models import Payment, Collect
from fundraising.services import pay


class PaySerializer(serializers.ModelSerializer):
    """
    Создание платежа
    """
    class Meta:
        model = Payment
        fields = [
            'pay_to',
            'payer',
            'sum',
        ]

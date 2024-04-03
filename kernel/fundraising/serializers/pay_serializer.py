# -*- coding: utf-8 -*-

from rest_framework import serializers

from fundraising.models import Payment, Collect
from fundraising.services import pay


class PaySerializer(serializers.Serializer):
    """
    Создание платежа
    """

    payer_id = serializers.IntegerField()
    pay_to = serializers.PrimaryKeyRelatedField(queryset=Collect.objects.all())
    summ = serializers.FloatField()

    def create(self, validated_data):
        payment = pay(
            payer=validated_data['payer_id'],
            pay_to=validated_data['pay_to'],
            sum=validated_data['summ']
        )

        return payment

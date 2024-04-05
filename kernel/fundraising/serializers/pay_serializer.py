# -*- coding: utf-8 -*-

from rest_framework import serializers

from fundraising.models import Payment, Collect
from fundraising.services import update_payment

from utils import send_email_about_payment as mail

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

    def create(self, validated_data):
        # Получаем данные из validated_data
        pay_to = validated_data.get('pay_to')
        payer = validated_data.get('payer')
        sum = validated_data.get('sum')

        # Проверяем статус сбора
        collect_obj = Collect.objects.get(id=pay_to.id)
        if not collect_obj.status:
            raise serializers.ValidationError("Сбор закрыт")

        payment = Payment.objects.create(pay_to=pay_to, payer=payer, sum=sum)

        update_payment(payment=payment, sum=sum)
        mail(payment=payment)

        return payment

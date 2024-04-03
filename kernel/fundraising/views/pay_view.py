# -*- coding: utf-8 -*-

from rest_framework import status, generics
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from fundraising.serializers import PaySerializer


class PayAPIView(generics.CreateAPIView):
    serializer_class = PaySerializer

    @extend_schema(
        summary='Выполнить новый платеж',
        description='Создает новый платеж',
        request=PaySerializer,
        responses={
            status.HTTP_200_OK: "Платеж выполнен",
            status.HTTP_400_BAD_REQUEST: "Неверные данные",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Ошибка платежа"
        }
    )
    def post(self, request, *arg, **kwargs):
        return self.create(request, *arg, **kwargs)

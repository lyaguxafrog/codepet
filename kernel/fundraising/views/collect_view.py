# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from fundraising.models import Collect
from users.models import UserProfile
from fundraising.services import stop_collect
from fundraising.serializers import CreateCollectSerializer



class CreateCollectView(generics.CreateAPIView):
    queryset = Collect.objects.all()
    serializer_class = CreateCollectSerializer



class StopCollectView(APIView):
    """
    API представление для остановки сбора.
    """

    @extend_schema(
        summary='Остановить сбор',
        description='Останавливает сбор по его ID.',
        parameters=[
            OpenApiParameter(
                name='collect_id',
                description='ID сбора, который нужно остановить.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True
            ),
            OpenApiParameter(
                name='owner_id',
                description='ID владельца сбора',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True
            ),
        ],
        responses={
            status.HTTP_200_OK: 'Сбор успешно остановлен.',
            status.HTTP_404_NOT_FOUND: 'Сбор с указанным ID не найден.',
            status.HTTP_500_INTERNAL_SERVER_ERROR: 'Произошла ошибка при остановке сбора.'
        }
    )
    def post(self, request, *args, **kwargs):
        """
        Останавливает сбор по его ID.

        :param request: Запрос на остановку сбора.
        :return: Ответ с результатом операции.
        """
        try:
            # Получаем экземпляр сбора
            collect_id = kwargs.get('collect_id')
            owner_id = kwargs.get('owner_id')
            if not collect_id or not owner_id:
                return Response({"error": "Не указаны ID сбора или владельца."},
                                status=status.HTTP_400_BAD_REQUEST)

            collect = Collect.objects.get(id=collect_id)
            # Получаем владельца сбора из запроса
            owner = UserProfile.objects.get(id=owner_id)

            # Вызываем сервис для остановки сбора
            updated_collect = stop_collect(collect, owner)

            # Возвращаем успешный ответ
            return Response({"message": "Сбор успешно остановлен."},
                            status=status.HTTP_200_OK)

        except Collect.DoesNotExist:
            return Response({"error": "Сбор с указанным ID не найден."},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

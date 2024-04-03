# -*- coding: utf-8 -*-

from django.urls import path
from fundraising.views import CreateCollectView, StopCollectView, PayAPIView

urlpatterns = [
    path('create/',
         CreateCollectView.as_view(), name='create_collect'),
    path('stop/<int:collect_id>/<int:owner_id>/',
         StopCollectView.as_view(), name='stop_collect'),
    path('pay/', PayAPIView.as_view(), name='payment'),
]

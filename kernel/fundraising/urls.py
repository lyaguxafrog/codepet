# -*- coding: utf-8 -*-

from django.urls import path
from fundraising.views import CreateCollectView

urlpatterns = [
    path('collects/create/',
         CreateCollectView.as_view(), name='create_collect'),
]

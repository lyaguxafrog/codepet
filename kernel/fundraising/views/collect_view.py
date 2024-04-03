# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from fundraising.serializers import CreateCollectSerializer
from fundraising.models import Collect

class CreateCollectView(generics.CreateAPIView):
    queryset = Collect.objects.all()
    serializer_class = CreateCollectSerializer

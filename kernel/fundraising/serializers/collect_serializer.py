# -*- coding: utf-8 -*-

from rest_framework import serializers

from fundraising.models import Collect
from users.models import UserProfile


class CreateCollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collect
        fields = [
            'id',
            'collect_owner',
            'collect_name',
            'reason',
            'description',
            'collect_goal',
            'collected_sum',
            'person_count',
            'cover',
            'end_date',
            'status'
        ]
        read_only_fields = ['collected_sum', 'person_count', 'create_date', 'status']

    def create(self, validated_data):
        collect_owner = validated_data.get('collect_owner')
        if not isinstance(collect_owner, UserProfile):
            raise serializers.ValidationError("collect_owner должен быть экземпляром UserProfile")

        collect = Collect.objects.create(**validated_data)
        return collect

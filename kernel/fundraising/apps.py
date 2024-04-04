# -*- coding: utf-8 -*-

from django.apps import AppConfig


class FundraisingConfig(AppConfig):
    name = 'fundraising'
    label = 'fundraising'
    verbose_name='Платежи и сборы'

    def ready(self) -> None:
        from fundraising.signals import close_collect_if_goal_reached
        return super().ready()

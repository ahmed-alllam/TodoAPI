#   Copyright (c) Code Written and Tested by Ahmed Emad in 02/03/2020, 12:30

from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        import core.signals

#   Copyright (c) Code Written and Tested by Ahmed Emad in 29/02/2020, 15:59
#

from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        import core.signals

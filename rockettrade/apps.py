from django.apps import AppConfig


class RockettradeConfig(AppConfig):
    name = 'rockettrade'

    def ready(self):
        import rockettrade.signals

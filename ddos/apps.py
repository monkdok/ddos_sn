from django.apps import AppConfig


class DdosConfig(AppConfig):
    name = 'ddos'

    def ready(self):
        import ddos.signals

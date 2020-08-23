from django.apps import AppConfig


class DdosConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals

from django.apps import AppConfig


class DdosConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals


class ActivitylogConfig(AppConfig):
    name = 'activitylog'

    def ready(self):
        from .api.signals import log_user_logged_in_failed, log_user_logged_in_success

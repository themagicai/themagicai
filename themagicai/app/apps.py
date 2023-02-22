from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'themagicai.app'

    def ready(self):
        try:
            import themagicai.app.signals  # noqa F401
        except ImportError:
            pass


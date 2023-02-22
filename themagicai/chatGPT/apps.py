from django.apps import AppConfig


class ChatgptConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "themagicai.chatGPT"

    def ready(self):
        try:
            import themagicai.chatGPT.signals  # noqa F401
        except ImportError:
            pass

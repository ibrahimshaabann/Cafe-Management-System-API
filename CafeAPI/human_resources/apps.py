from django.apps import AppConfig


class HumanResourcesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'human_resources'
    def ready(self):
        import human_resources.signals
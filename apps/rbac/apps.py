from django.apps import AppConfig


class RbacConfig(AppConfig):
    name = 'apps.rbac'

    def ready(self):
        from .signals import create_user

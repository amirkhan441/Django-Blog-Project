# Register the signals in the users app

from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
        # Call the function to ensure default image exists
        from users.signals import ensure_default_image_exists
        ensure_default_image_exists()
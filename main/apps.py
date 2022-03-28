from django.apps import AppConfig


class MainConfig(AppConfig):
    """
    Configuration Class for the SEO App
    Extends django.apps.AppConfig
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

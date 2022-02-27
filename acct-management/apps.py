from django.apps import AppConfig


class AcctManagementConfig(AppConfig):
    """
    Configuration Class for Account Management App
    Extends django.apps.AppConfig
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'acct-management'

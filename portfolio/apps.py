from django.apps import AppConfig
from django import template

register = template.Library()


class PortfolioConfig(AppConfig):
    """Configs for the portfolio(main) app"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'

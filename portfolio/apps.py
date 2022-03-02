from django.apps import AppConfig
from django import template

register = template.Library()


class PortfolioConfig(AppConfig):
    """Configs for the portfolio(main) app"""

    name = 'portfolio'

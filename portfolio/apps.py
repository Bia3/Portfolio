from django.apps import AppConfig
from django import template

register = template.Library()


class PortfolioConfig(AppConfig):
    name = 'portfolio'

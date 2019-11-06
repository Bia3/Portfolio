from django.apps import AppConfig
from django import template

register = template.Library()


class RossdevsConfig(AppConfig):
    name = 'RossDevs'

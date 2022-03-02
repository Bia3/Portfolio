from django import template
from markdownx.utils import markdownify as markdownifyx

register = template.Library()


@register.filter(is_safe=True)
def markdownify(value):
    """
    Filter to compile markdown to html
    :param value:
    :return:
    """
    return markdownifyx(value)

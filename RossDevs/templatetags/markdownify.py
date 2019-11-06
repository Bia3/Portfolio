from ..apps import register
from markdownx.utils import markdownify as markdownifyx


@register.filter
def markdownify(value):
    return markdownifyx(value)

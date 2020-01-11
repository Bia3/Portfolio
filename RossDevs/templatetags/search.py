from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from ..models import Svg

register = template.Library()


@register.simple_tag
def svg_by_name(val):
    svg = Svg.objects.get(name=val)
    if svg:
        return mark_safe("{}".format(svg.data))
    else:
        return mark_safe("<span>Unable to find SVG</span>")

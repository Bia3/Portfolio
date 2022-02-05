from django import template
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from ..models import Svg

register = template.Library()


@register.simple_tag
def svg_by_name(svg_name):
    print(svg_name)
    try:
        svg = Svg.objects.get(name=svg_name)
        return mark_safe("{}".format(svg.data))
    except Svg.DoesNotExist:
        return mark_safe("<span>Unable to find SVG</span>")


@register.simple_tag
def footer_icon(txt, link, svg_name):
    templ = 'footer_ico_link.html'
    context = {
        'txt': txt,
        'link': link,
        'svg_name': svg_name
    }
    resp = render(request=None, template_name=templ, context=context)
    resp = render_to_string(template_name=templ, context=context)
    return mark_safe(resp)
    # return f'{txt}, {link}, {svg_name}'

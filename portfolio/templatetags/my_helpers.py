from django import template
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.contrib.staticfiles import finders
from ..models import Svg

register = template.Library()


@register.simple_tag
def svg_by_name(svg_name):
    """
    Tag to return svg from database
    :param svg_name:
    :return:
    """
    # ToDo: This tag needs review for possible cross site scripting issues
    try:
        svg = Svg.objects.get(name=svg_name)
        return mark_safe("{}".format(svg.data))
    except Svg.DoesNotExist:
        try:
            fname = f'{svg_name}.svg'
            result = finders.find(f'portfolio/svgs/{fname}')
            if result:
                with open(result, 'r') as file:
                   data = file.read()
                return mark_safe(f'<span>{data}</span>')
        except IOError:
            return mark_safe(f'<span>Unable to find SVG<br />{result}</span>')


@register.simple_tag
def footer_icon(txt, link, svg_name):
    """
    Tag to generate footer icons
    :param txt:
    :param link:
    :param svg_name:
    :return:
    """
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

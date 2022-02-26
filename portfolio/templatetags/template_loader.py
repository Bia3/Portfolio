from django.template.defaultfilters import stringfilter
from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.filter
@stringfilter
def lower(value):
    return value.lower()


@register.simple_tag
def home_header():
    return render_to_string('home_header.html')


@register.simple_tag
def standard_header():
    return render_to_string('header.html')


@register.simple_tag
def home_footer():
    return render_to_string('home_footer.html')


@register.simple_tag
def standard_footer():
    return render_to_string('footer.html')


@register.simple_tag
def small_header():
    return render_to_string('small_header.html')

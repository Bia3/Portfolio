from django.template.defaultfilters import stringfilter
from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.filter
@stringfilter
def lower(value):
    """
    Filter to transform text to lower characters only
    :param value: String
    :return: String
    """
    return value.lower()


@register.simple_tag
def large_header(md, bio):
    """
    Tag to render the large_header template
    :param md: String
    :param bio: String
    :return: String
    """
    return render_to_string('large_header.html', {'bio': bio, 'md': md})


@register.simple_tag
def standard_header():
    """
    Tag to render the header template
    :return: String
    """
    return render_to_string('header.html')


@register.simple_tag
def large_footer():
    """
    Tag to render the large_footer template
    :return: String
    """
    return render_to_string('large_footer.html')


@register.simple_tag
def standard_footer():
    """
    Tag to render the footer template
    :return: String
    """
    return render_to_string('footer.html')


@register.simple_tag
def small_header():
    """
    Tag to render the small_header template
    :return: String
    """
    return render_to_string('small_header.html')

from django import template
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.contrib.staticfiles import finders
from django.contrib.auth.models import User
from acct_management.models import ContactCard


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
        f_name = f'{svg_name}.svg'
        result = finders.find(f'portfolio/svgs/{f_name}')
        if result:
            with open(result, 'r') as file:
                data = file.read()
            return mark_safe(f'<span>{data}</span>')
    except IOError:
        return mark_safe('<span>Unable to find SVG</span>')


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
    # resp = render(request=None, template_name=templ, context=context)
    resp = render_to_string(template_name=templ, context=context)
    return mark_safe(resp)
    # return f'{txt}, {link}, {svg_name}'


@register.simple_tag
def socials():
    """
    Tag to load all the social icons for the footer
    """
    templ = 'social.html'
    main_user = User.objects.filter(
        groups__name__contains='primary_account').first()

    cc = ContactCard.objects.filter(user=main_user).first()

    socs = []
    if cc:
        socs += [{'txt': f'{soc.username}', 'link': soc.link,
                  'svg_name': 'GitHub'} for soc in cc.github_set.all()]

        socs += [{'txt': f'{soc.username}', 'link': soc.link,
                  'svg_name': 'Keybase'} for soc in cc.keybase_set.all()]

        socs += [{'txt': f'{soc.username}', 'link': soc.link,
                  'svg_name': 'CodeWars'} for soc in cc.codewars_set.all()]

        socs += [{'txt': f'{soc.username}', 'link': soc.link,
                  'svg_name': 'CodePen'} for soc in cc.codepen_set.all()]

        socs += [{'txt': f'{soc.username}', 'link': soc.link,
                  'svg_name': 'LinkedIn'} for soc in cc.linkedin_set.all()]

        socs += [{'txt': f'{soc.username}', 'link': soc.link, 'svg_name': 'HTB'}
                 for soc in cc.hackthebox_set.all()]

    if main_user:
        email = main_user.email
        socs.append(
            {'txt': f'{email}', 'link': f'{email}', 'svg_name': 'Email'})

    context = {
        'socials': socs
    }
    response = render_to_string(template_name=templ, context=context)
    if socs:
        return mark_safe(response)
    return ''

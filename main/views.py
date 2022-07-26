
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.decorators.http import require_GET


class CodeOfConductView(View):
    template_name = 'code_of_conduct.html'

    def get(self, request, *args, **kwargs):
        try:
            with open('./docs/CODE_OF_CONDUCT.md', 'r') as file:
                coc = file.read()
        except FileNotFoundError as error:
            return HttpResponse(status=500)

        context = {
            'md': coc
        }

        return render(request, self.template_name, context)


class PrivacyPolicyView(View):
    template_name = 'privacy.html'

    def get(self, request, *args, **kwargs):
        try:
            with open('./docs/Privacy.md', 'r') as file:
                privacy = file.read()
        except FileNotFoundError as error:
            return HttpResponse(status=500)

        context = {
            'md': privacy
        }

        return render(request, self.template_name, context)


class SecurityPolicyView(View):
    template_name = 'security.html'

    def get(self, request, *args, **kwargs):
        try:
            with open('./docs/Security.md', 'r') as file:
                sec = file.read()
        except FileNotFoundError as error:
            return HttpResponse(status=500)

        context = {
            'md': sec
        }

        return render(request, self.template_name, context)


class AboutView(View):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class SiteMapView(View):
    template_name = 'sitemap.html'
    context = {
        'sites': []
    }
    static = [
        'home',
        'resume',
        'curriculum_vitae',
        'projects'
    ]

    def get(self, request, *args, **kwargs):
        self.context['sites'] = self.static
        return render(request, self.template_name, self.context)


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')

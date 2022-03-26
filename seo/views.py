
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


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

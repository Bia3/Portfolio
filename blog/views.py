from django.shortcuts import render
from django.views import View


class BlogHomeView(View):
    """View class for the blog's homepage"""
    template = 'blog_home.html'

    def get(self, request, *args, **kwargs):
        """
        Function to handle GET requests for the Blog Homepage
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return render(request, self.template, {})

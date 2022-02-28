from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class LogOutView(View):
    """
    Class based View for the logout page
    Extends django.views.View
    """

    @staticmethod
    def get(request):
        """
        GET View for logout Page
        redirects to home page
        :param request:
        :return:
        """
        logout(request)
        return redirect('home')

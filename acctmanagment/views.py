from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class LogOutView(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect('home')

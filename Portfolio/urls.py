"""
Primary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from portfolio import views
from portfolio import urls as portfolio_urls


handler404 = 'portfolio.views.handler404'
handler500 = 'portfolio.views.handler500'

urlpatterns = [
    url('s3cr3t/', admin.site.urls),
    url('accounts/', include('acct_management.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url('portfolio/', include(portfolio_urls)),
    url('forms/addachievement', views.AddAchievementFormView.as_view(),
        name='add_achievement_form'),
    url('forms/add_skill', views.AddSkillFormView.as_view(), name='add_skill_form'),
    url('forms/add_project', views.AddProjectFormView.as_view(),
        name='add_project_form'),
]

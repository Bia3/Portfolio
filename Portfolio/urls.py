"""Portfolio URL Configuration

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
# from django.urls import include, re_path
from django.contrib import admin
from django.urls import path
from RossDevs.views import *


handler404 = 'RossDevs.views.handler404'
handler500 = 'RossDevs.views.handler500'

urlpatterns = [
    url('s3cr3t/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    url('accounts/', include('acctmanagment.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url('forms/addachievement', AddAchievementFormView.as_view(), name='add_achievement_form'),
    url('forms/add_skill', AddSkillFormView.as_view(), name='add_skill_form'),
    url('forms/add_project', AddProjectFormView.as_view(), name='add_project_form'),
    # url('^projects/$', ProjectsView.as_view()),
    # url('^projects/[a-z]+/$', ProjectView.as_view()),
    # url('^resume/$', ResumeView.as_view()),
    # url('^cv/$', CurriculumVitaeView.as_view()),
]

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Bio, ContactCard, Resume, CurriculumVitae, Project
from markdownx.utils import markdownify


# Create your views here.
class HomeView(View):
    bio = Bio.objects.first()
    contact = ContactCard.objects.first()
    md = ''
    if bio:
        md = markdownify(bio.mark_down)

    def get(self, request):
        return render(request, 'home.html', {
            'bio': self.bio,
            'md': self.md,
            'contact': self.contact,
        })


class CurriculumVitaeView(View):
    cvs = CurriculumVitae.objects.all()

    def get(self, request):
        return render(request, 'curriculum_vitae.html', {
            'cvs': self.cvs,
        })


class ProjectsView(View):
    projects = Project.objects.all()

    def get(self, request):
        return render(request, 'projects.html', {
            'projects': self.projects
        })


class ResumeView(View):
    resume = Resume.objects.first()

    def get(self, request):
        return render(request, 'resume.html', {
            'resume': self.resume
        })

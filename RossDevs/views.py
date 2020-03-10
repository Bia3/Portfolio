from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import ContactCard, Resume, CurriculumVitae, Project, Bio
from markdownx.utils import markdownify


# Create your views here.
class HomeView(View):
    bio = ""
    contact = ""
    md = ""

    def get(self, request):
        self.bio = Bio.objects.first()
        self.contact = ContactCard.objects.first()
        if self.bio:
            self.md = markdownify(self.bio.mark_down)
        return render(request, 'home.html', {
            'bio': self.bio,
            'md': self.md,
            'contact': self.contact
        })


class CurriculumVitaeView(View):
    cvs = ""

    def get(self, request):
        self.cvs = CurriculumVitae.objects.all()
        return render(request, 'curriculum_vitae.html', {
            'cvs': self.cvs,
        })


class ProjectsView(View):
    projects = ""

    def get(self, request):
        self.projects = Project.objects.all()
        return render(request, 'projects.html', {
            'projects': self.projects
        })


class ProjectView(View):
    project = ""

    def get(self, request):
        self.project = Project.objects.get()
        return render(request, 'project.html', {
            'project': self.project
        })


class ResumeView(View):
    resume = ""

    def get(self, request):
        self.resume = Resume.objects.first()
        return render(request, 'resume.html', {
            'resume': self.resume
        })


def custom_404(request):
    return render(request, '404.html', {}, status=404)
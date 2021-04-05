import string

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import ContactCard, Resume, CurriculumVitae, Project, Bio, Skill, Achievement
from markdownx.utils import markdownify

mobile_browsers = [
    'Android',
    'webOS',
    'iPhone',
    'iPad',
    'iPod',
    'BlackBerry',
    'IEMobile',
    'Opera Mini'
]

desktop_browsers = [
    'Mac',
    'Macintosh',
    'Linux',
    'Windows'
]

# Create your views here.
class HomeView(View):
    bio = ""
    contact = ""
    md = None
    projects = ""
    skills_raw = []
    skills = []
    achieves_raw = []
    achieves = []

    def get(self, request):
        self.bio = Bio.objects.first()
        self.contact = ContactCard.objects.first()
        self.projects = Project.objects.all()
        self.skills_raw = Skill.objects.all()
        self.skills = []
        self.achieves_raw = Achievement.objects.all().order_by('order')
        self.achieves = []

        if self.bio:
            self.md = markdownify(self.bio.mark_down)

        if len(self.skills_raw) >= 1:
            for skill in self.skills_raw:
                self.skills.append({
                    'id': skill.id,
                    'name': skill.name,
                    'description': markdownify(skill.description),
                    'highlights': markdownify(skill.highlights)
                })

        if len(self.skills_raw) >= 1:
            for achieve in self.achieves_raw:
                self.achieves.append({
                    'id': achieve.id,
                    'name': achieve.name,
                    'description': markdownify(achieve.description)
                })
        http_user = self.request.META['HTTP_USER_AGENT']
        http_user_clean = http_user.translate(str.maketrans('', '', string.punctuation))
        if any(item in http_user_clean.split(' ') for item in mobile_browsers):
            return render(request, 'home.html', {
                'bio': self.bio,
                'md': self.md,
                'contact': self.contact,
                'projects': self.projects,
                'skills': self.skills,
                'achieves': self.achieves,
                'style': 'RossDevs/css/m_style.css',
            })
        elif any(item in http_user_clean.split(' ') for item in desktop_browsers):
            print('desktop')
        print(self.request.META['HTTP_USER_AGENT'].translate(str.maketrans('', '', string.punctuation)))

        return render(request, 'home.html', {
            'bio': self.bio,
            'md': self.md,
            'contact': self.contact,
            'projects': self.projects,
            'skills': self.skills,
            'achieves': self.achieves,
            'style': 'RossDevs/css/style.css',
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


def custom_404(View, request):
    return render(request, '404.html', {}, status=404)


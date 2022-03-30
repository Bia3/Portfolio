import string

from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q

from .forms import AchievementForm, SkillForm, ProjectForm
from acct_management.models import Bio, ContactCard
from .models import CurriculumVitae,\
    Project,\
    Skill,\
    Achievement, \
    Education
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


class HomeView(View):
    """Class based View for the Home Page"""

    bio = ""
    contact = ""
    md = None
    skills_raw = []
    skills = []
    achieves_raw = []
    achieves = []

    def __init__(self, **kwargs):
        super().__init__()
        self.main_user = User.objects.filter(
            groups__name__contains='primary_account').first()

    def get(self, request, *args, **kwargs):
        """
        Function to handle GET requests to the Home Page
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.bio = Bio.objects.filter(user=self.main_user).first()
        self.skills_raw = Skill.objects.all()
        self.skills = []
        self.achieves_raw = Achievement.objects.order_by('-completed')
        self.achieves = []

        if self.bio:
            self.md = markdownify(self.bio.copy)

        if len(self.skills_raw) >= 1:
            for skill in self.skills_raw:
                self.skills.append({
                    'id': skill.id,
                    'name': skill.title,
                    'description': skill.summary
                })

        if len(self.skills_raw) >= 1:
            for achieve in self.achieves_raw:
                self.achieves.append({
                    'id': achieve.id,
                    'name': achieve.title,
                    'description': achieve.summary
                })
        http_user = self.request.META['HTTP_USER_AGENT']
        http_user_clean = http_user.translate(
            str.maketrans('', '', string.punctuation))
        if any(item in http_user_clean.split(' ') for item in mobile_browsers):
            return render(request, 'home.html', {
                'bio': self.bio,
                'md': self.md,
                'skills': self.skills,
                'achieves': self.achieves,
                'style': 'RossDevs/css/m_style.css',
            })
        print(self.request.META['HTTP_USER_AGENT'].translate(
            str.maketrans('', '', string.punctuation)))

        return render(request, 'home.html', {
            'bio': self.bio,
            'md': self.md,
            'skills': self.skills,
            'achieves': self.achieves,
            'style': 'RossDevs/css/style.css',
        })


class AddAchievementFormView(View):
    """Class based View to handle form requests for Achievements"""

    form_class = AchievementForm
    initial = {
        'name': 'value',
        'description': 'value',
        'order': 0
    }
    template_name = 'form_template.html'

    # Create the default form.
    def get(self, request, *args, **kwargs):
        """
        Function to handle GET requests for the Achievements Form
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = self.form_class(initial=self.initial)
        return render(request, 'achievement_form_template.html', {'form': form})

    # Process the Form data
    def post(self, request, *args, **kwargs):
        """
        Function to handle POST requests for the Achievements Form
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # Create a form instance and populate it with data from the request (binding):
        form = self.form_class(request.POST)

        if form.is_valid():
            new_achievement = Achievement(form.cleaned_data)
            new_achievement.save()
        return render(request, 'achievement_form_template.html', {'form': form})


class AddSkillFormView(View):
    """Class based View to handle form requests for Skills"""

    form_class = SkillForm
    initial = {
    }
    template_name = 'skill_form_template.html'

    # Create the default form.
    def get(self, request, *args, **kwargs):
        """
        Function to handle GET requests for the Skills Form
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'success': 'false'})

    # Process the Form data
    def post(self, request, *args, **kwargs):
        """
        Function to handle POST requests for the Skills Form
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # Create a form instance and populate it with data from the request (binding):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_skill = Skill(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                highlights=form.cleaned_data['highlights'],
            )
            new_skill.save()
        return render(request, self.template_name, {
            'form': form,
            # if form is valid set the js variable "form_complete" to ture else false
            'success': ('true' if form.is_valid() else 'false')
        })


class AddProjectFormView(View):
    """Class based View to handle form requests for Projects"""

    form_class = ProjectForm
    initial = {
    }
    template_name = 'project_form_template.html'

    # Create the default form.
    def get(self, request, *args, **kwargs):
        """
        Function to handle GET requests for the Projects Form
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'success': 'false'})

    # Process the Form data
    def post(self, request, *args, **kwargs):
        """
        Function to handle POST requests for the Projects Form
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # Create a form instance and populate it with data from the request (binding):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_obj = Project(
                name=form.cleaned_data['name'],
                short_desc=form.cleaned_data['short_desc'],
                git_link=form.cleaned_data['git_link'],
            )
            new_obj.save()
        return render(request, self.template_name, {
            'form': form,
            # if form is valid set the js variable "form_complete" to ture else false
            'success': ('true' if form.is_valid() else 'false')
        })


class CurriculumVitaeView(View):
    """
    Class based view for the Curriculum Vitae
    (course of one’s life) page
    """

    cv = {}
    bio = {}
    contact_card = {}
    address = {}
    ed = []
    certs = []
    skills = []
    professional_experiences = []
    field_experiences = []
    professional_development = []

    def __init__(self, **kwargs):
        super().__init__()
        self.main_user = User.objects.filter(
            groups__name__contains='primary_account').first()

    def get(self, request, *args, **kwargs):
        """
        Function to handle GET requests for the Curriculum Vitae Page
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.cv = CurriculumVitae.objects.filter(user=self.main_user).first()
        self.bio = Bio.objects.filter(user=self.main_user).first()
        self.contact_card = ContactCard.objects.filter(user=self.main_user).first()
        self.address = self.contact_card.address if (hasattr(self.contact_card, 'address') if self.contact_card else None) else None
        self.ed = Education.objects.filter(
            cv=self.cv).filter(certificate=False)
        self.certs = Education.objects.filter(
            cv=self.cv).filter(certificate=True)
        self.skills = Skill.objects.filter(cv=self.cv)
        self.professional_experiences = Achievement.objects.filter(
            work_experience__cv=self.cv)
        self.field_experiences = Achievement.objects.filter(project__field_experience=True)\
            .filter(project__user=self.main_user)
        self.professional_development = Achievement.objects.filter(
            Q(course_work__course__education__in=self.ed) |
            (Q(project__professional_development=True)
             & Q(project__user=self.main_user))
        )

        return render(request, 'curriculum_vitae.html', {
            'name': self.main_user.get_full_name() if self.main_user else '',
            'profession': self.bio.profession if self.bio else '',
            'cv': self.cv,
            'address': self.address,
            'education': self.ed,
            'certificates': self.certs,
            'skills': self.skills,
            'professional_experiences': self.professional_experiences,
            'field_experiences': self.field_experiences,
            'professional_development': self.professional_development
        })


class ProjectsView(View):
    """Class based View for the Projects page"""

    projects = []

    def get(self, request):
        """
        Function to handle GET requests for the Projects Page
        :param request:
        :return:
        """
        self.projects = Project.objects.all()
        return render(request, 'projects.html', {
            'projects': self.projects
        })


class ProjectView(View):
    """Class based View for a single Project page"""

    project = {}

    def get(self, request, *args, **kwargs):
        """
        Function to handle GET requests for the single Project Page
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.project = Project.objects.get()
        return render(request, 'project.html', {
            'project': self.project
        })


class ResumeView(View):
    """Class based View for the Resume Page"""

    resume = {}
    achievements = []

    def __init__(self, **kwargs):
        super().__init__()
        self.main_user = User.objects.filter(
            groups__name__contains='primary_account').first()

    def get(self, request, *args, **kwargs):
        """
        Function to handle Get requests for the Resume Page
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.resume = self.main_user.resume if self.main_user else None
        self.achievements = Achievement.objects.filter(
            Q(project__user=self.main_user) |
            Q(education__resume__user=self.main_user) |
            Q(work_experience__resume__user=self.main_user)
        )

        return render(request, 'resume.html', {
            'resume': self.resume,
            'achievements': self.achievements,
            'main_user_name': self.main_user.get_full_name() if self.main_user else '',
            'email': self.main_user.email if self.main_user else '',
            'phone': '(555) 555-5555',
            'website': 'https://www.rossdev.io'
        })


def handler404(request, *args, **argv):
    """
    Function based view to handle 404's
    :param request:
    :param args:
    :param argv:
    :return:
    """
    response = render(request, '404.html', {}, status=404)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    """
    Function based view to handle 500's
    :param request:
    :param args:
    :param argv:
    :return:
    """
    response = render(request, template_name='500.html',
                      context={}, status=500)
    response.status_code = 500
    return response

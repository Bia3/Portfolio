import uuid
from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField


class Resume(models.Model):
    """Resume template builder"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    summary = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.user.get_full_name()}\'s Resume'


class CurriculumVitae(models.Model):
    """Curriculum Vitae(CV) template builder"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.user.get_full_name()}\'s CV'


class Project(models.Model):
    """A project that proves you knowledge"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cv = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    copy = MarkdownxField(max_length=3000)
    short_summary = models.CharField(max_length=250)
    summary = models.TextField(max_length=500)
    professional_development = models.BooleanField(default=False)
    field_experience = models.BooleanField(default=False)
    github_link = models.CharField(max_length=250)
    completed = models.DateField

    def __str__(self):
        return self.title


class Skill(models.Model):
    """
    Skills related to learning and
    advancement in school or work
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, blank=True, null=True)
    cv = models.ForeignKey(
        CurriculumVitae, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=180)
    copy = MarkdownxField(max_length=3000)
    summary = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    """Jobs volunteer work and other professional experiences"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, blank=True, null=True)
    cv = models.ForeignKey(
        CurriculumVitae, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True)
    position = models.CharField(max_length=180)
    organization = models.CharField(max_length=180)
    summary = models.TextField(max_length=1000)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.position}: {self.organization}'


class Education(models.Model):
    """An educational institute or certificate attended and achieved"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    cv = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE)
    field_of_study = models.CharField(max_length=180)
    degree = models.CharField(max_length=180)
    institution = models.CharField(max_length=180)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f'{self.degree}: {self.institution}'


class Responsibility(models.Model):
    """Responsibilities performed at a Job"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    work_experience = models.ForeignKey(
        WorkExperience, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    short_summary = models.CharField(max_length=250)
    summary = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    """An achievement or accolade"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True)
    education = models.ForeignKey(
        Education, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=180)
    short_summary = models.CharField(max_length=250)
    summary = models.TextField(max_length=500)
    copy = MarkdownxField(max_length=3000)
    completed = models.DateField()

    def __str__(self):
        return self.title


class Course(models.Model):
    """A course taken through an educational institute"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    summary = models.TextField(max_length=500)
    end = models.DateField()

    def __str__(self):
        return self.title


class CourseWork(models.Model):
    """An assignment or project created as a part of a Course"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    short_summary = models.CharField(max_length=250)
    summary = models.TextField(max_length=500)
    copy = MarkdownxField(max_length=3000)

    def __str__(self):
        return self.title

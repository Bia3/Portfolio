import uuid
from django.db import models
from markdownx.models import MarkdownxField


class Skill(models.Model):
    name = models.CharField(max_length=100)
    language = models.BooleanField
    tool = models.BooleanField
    concept = models.BooleanField
    description = MarkdownxField(blank=True)
    highlights = MarkdownxField(blank=True)

    def __str__(self):
        return self.name


class Responsibility(models.Model):
    name = models.CharField(max_length=100)
    description = MarkdownxField(blank=True)
    related_skill = models.ManyToManyField(
        Skill,
        blank=True,
        verbose_name='related skill'
    )

    def __str__(self):
        return self.name


class Accomplishment(models.Model):
    name = models.CharField(max_length=100)
    highlights = MarkdownxField(blank=True)
    related_skill = models.ManyToManyField(
        Skill,
        blank=True,
        verbose_name='related skill'
    )
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    highlights = MarkdownxField(blank=True)
    responsibility = models.ManyToManyField(
        Responsibility,
        blank=True,
        verbose_name='responsibilities'
    )
    accomplishment = models.ManyToManyField(
        Accomplishment,
        blank=True,
        verbose_name='accomplishments'
    )
    start = models.DateField(blank=False)
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}: {}'.format(self.company, self.title)


class School(models.Model):
    name = models.CharField(max_length=100)
    graduated = models.BooleanField
    highlights = MarkdownxField(blank=True)
    start = models.DateField(blank=False)
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    title = models.CharField(max_length=100)
    shortend_md = MarkdownxField(blank=True)
    mark_down = MarkdownxField(blank=True)
    highlights = MarkdownxField(blank=True)
    related_skill = models.ManyToManyField(
        Skill,
        blank=True,
        verbose_name='related skill'
    )
    start = models.DateField(blank=False)
    end = models.DateField(blank=True, null=True)


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    highlights = MarkdownxField(blank=True)
    completion = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True)
    related_skill = models.ManyToManyField(
        Skill,
        blank=True,
        verbose_name='related skill'
    )

    def __str__(self):
        return self.title


class Resume(models.Model):
    job = models.ManyToManyField(
        Job,
        blank=True,
        verbose_name='Job History'
    )
    education = models.ManyToManyField(
        School,
        blank=True,
        verbose_name='Education History'
    )
    certificates = models.ManyToManyField(
        Certificate,
        blank=True,
        verbose_name='Certificates'
    )
    section = models.ManyToManyField(
        Section,
        blank=True,
        verbose_name='Extra Sections'
    )
    pdf = models.FileField(blank=True)
    expired = models.BooleanField(blank=False)
    creation = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField


class CodeSnippet(models.Model):
    name = models.CharField(max_length=30, blank=False)
    mark_down = MarkdownxField(blank=False)


class ProjectSection(models.Model):
    title = models.CharField(max_length=30, blank=False)
    mark_down = MarkdownxField(blank=False)


class Project(models.Model):
    uid = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=100)
    short_desc = MarkdownxField(blank=True)
    git_link = models.CharField(
        max_length=400,
        blank=True)
    files = models.ManyToManyField(
        File,
        blank=True,
        verbose_name='Project Files'
    )
    code_snippets = models.ManyToManyField(
        CodeSnippet,
        blank=True,
        verbose_name='Project Code Snippets'
    )
    mark_down_sections = models.ManyToManyField(
        ProjectSection,
        blank=True,
        verbose_name='Project Description Sections'
    )


class CurriculumVitae(models.Model):
    name = models.CharField(max_length=100)
    mark_down = MarkdownxField(blank=True)
    job = models.ManyToManyField(
        Job,
        blank=True,
        verbose_name='Job History'
    )
    education = models.ManyToManyField(
        School,
        blank=True,
        verbose_name='Education History'
    )
    section = models.ManyToManyField(
        Section,
        blank=True,
        verbose_name='Extra Sections'
    )
    accomplishment = models.ManyToManyField(
        Accomplishment,
        blank=True,
        verbose_name='Accomplishments'
    )
    projects = models.ManyToManyField(
        Project,
        blank=True,
        verbose_name='Projects'
    )
    certificates = models.ManyToManyField(
        Certificate,
        blank=True,
        verbose_name='Certificates'
    )
    skills = models.ManyToManyField(
        Skill,
        blank=True,
        verbose_name='Skills'
    )
    date = models.DateField(blank=False)


class Bio(models.Model):
    title = models.CharField(max_length=100)
    mark_down = MarkdownxField(blank=True)
    creation = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    expired = models.BooleanField(blank=False)

    def __str__(self):
        return '{}'.format(self.title)


class ContactCard(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    po_box = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=30, blank=True)
    expired = models.BooleanField(blank=False)


class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = MarkdownxField(blank=True)
    order = models.IntegerField(unique=True)


class Svg(models.Model):
    name = models.CharField(max_length=30, blank=False)
    data = models.TextField(blank=False)

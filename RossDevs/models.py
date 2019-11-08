from django.db import models
from markdownx.models import MarkdownxField


class Skill(models.Model):
    name = models.CharField(max_length=30)
    language = models.BooleanField
    tool = models.BooleanField
    concept = models.BooleanField
    description = MarkdownxField(blank=True)
    highlights = MarkdownxField(blank=True)


class Responsibility(models.Model):
    name = models.CharField(max_length=30)
    description = MarkdownxField(blank=True)
    related_skill = models.ManyToManyField(
        Skill,
        blank=True,
        verbose_name='related skill'
    )


class Accomplishment(models.Model):
    name = models.CharField(max_length=30)
    highlights = MarkdownxField(blank=True)
    related_skill = models.ManyToManyField(
        Skill,
        blank=True,
        verbose_name='related skill'
    )
    end = models.DateField(blank=True)


class Job(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
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
    end = models.DateField(blank=True)


class School(models.Model):
    name = models.CharField(max_length=30)
    graduated = models.BooleanField
    highlights = MarkdownxField(blank=True)
    start = models.DateField(blank=False)
    end = models.DateField(blank=True)


class Section(models.Model):
    title = models.CharField(max_length=30)
    shortend_md = MarkdownxField(blank=True)
    mark_down = MarkdownxField(blank=True)
    highlights = MarkdownxField(blank=True)
    related_skill = models.ManyToManyField(
        Skill,
        blank=True,
        verbose_name='related skill'
    )
    start = models.DateField(blank=False)
    end = models.DateField(blank=True)


class Certificate(models.Model):
    title = models.CharField(max_length=30)
    highlights = MarkdownxField(blank=True)
    completion = models.DateField(blank=True)
    image = models.ImageField(blank=True)
    related_skill = models.ManyToManyField(
        Skill,
        blank=True,
        verbose_name='related skill'
    )


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
    creation = models.DateTimeField(auto_now_add=True, blank=True)


class File(models.Model):
    name = models.CharField(max_length=30)
    file = models.FileField


class CodeSnippet(models.Model):
    name = models.CharField(max_length=30)
    snippet = models.TextField


class ProjectSection(models.Model):
    title = models.CharField(max_length=30)
    mark_down = models.TextField


class Project(models.Model):
    name = models.CharField(max_length=30)
    highlights = MarkdownxField(blank=True)
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
    name = models.CharField(max_length=30)
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
    title = models.CharField(max_length=30)
    mark_down = MarkdownxField(blank=True)
    creation = models.DateTimeField(auto_now_add=True, blank=True)
    expired = models.BooleanField(blank=False)


class ContactCard(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    po_box = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=30, blank=True)
    expired = models.BooleanField(blank=False)

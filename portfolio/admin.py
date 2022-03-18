from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import CurriculumVitae, Resume, Project, Skill, WorkExperience, \
    Education, Responsibility, Course, CourseWork, Achievement


def username_from_project(proj):
    return proj.user.username


def username_from_resume(res):
    return res.user.username


def username_from_cv(cv):
    return cv.user.username


def username_from_work_experience(we):
    if we.resume:
        return username_from_resume(we.resume)
    if we.project:
        return username_from_project(we.project)
    if we.cv:
        return username_from_cv(we.cv)
    return 'None'


def username_from_education(ed):
    if ed.resume:
        return username_from_resume(ed.resume)
    if ed.cv:
        return username_from_cv(ed.cv)
    return 'None'


def username_from_skill(sk):
    if sk.project:
        return username_from_project(sk.project)
    if sk.resume:
        return username_from_resume(sk.resume)
    if sk.cv:
        return username_from_cv(sk.cv)
    return 'None'


def username_from_achievement(ach):
    if ach.project:
        return username_from_project(ach.project)
    if ach.education:
        return username_from_education(ach.education)
    return 'None'


@admin.register(Skill)
class SkillAdmin(MarkdownxModelAdmin):
    """Display settings for the Skill model on the Admin page"""

    list_display = ('title', 'view_username', 'id')

    @staticmethod
    def view_username(obj):
        return username_from_skill(obj)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    """Display settings for the Resume model on the Admin page"""

    list_display = ('view_username', 'id')

    @staticmethod
    def view_username(obj):
        return username_from_resume(obj)


@admin.register(CurriculumVitae)
class CurriculumVitaeAdmin(admin.ModelAdmin):
    """Display settings for the CurriculumVitae model on the Admin page"""

    list_display = ('id', )


@admin.register(Responsibility)
class ResponsibilityAdmin(MarkdownxModelAdmin):
    """Display settings for the Responsibility model on the Admin page"""

    list_display = ('id', )


@admin.register(WorkExperience)
class WorkExperienceAdmin(MarkdownxModelAdmin):
    """Display settings for the WorkExperience model on the Admin page"""

    list_display = ('view_username', 'organization', 'position', 'start', 'end', 'id')

    @staticmethod
    def view_username(obj):
        return username_from_work_experience(obj)


@admin.register(Education)
class EducationAdmin(MarkdownxModelAdmin):
    """Display settings for the Education model on the Admin page"""

    list_display = ('id', )


@admin.register(Course)
class CourseAdmin(MarkdownxModelAdmin):
    """Display settings for the Course model on the Admin page"""

    list_display = ('id', )


@admin.register(CourseWork)
class CourseWorkAdmin(MarkdownxModelAdmin):
    """Display settings for the CourseWork model on the Admin page"""

    list_display = ('id', )


@admin.register(Project)
class ProjectAdmin(MarkdownxModelAdmin):
    """Display settings for the Project model on the Admin page"""

    list_display = ('id', )


@admin.register(Achievement)
class AchievmentAdmin(admin.ModelAdmin):
    """Display settings for the Achievement model on the Admin Page"""

    list_display = ('title', 'view_username', 'completed', 'id')

    @staticmethod
    def view_username(obj):
        username_from_achievement(obj)

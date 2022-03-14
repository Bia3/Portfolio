from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import CurriculumVitae, Resume, Project, Skill, WorkExperience, \
    Education, Responsibility, Course, CourseWork, Achievement


@admin.register(Skill)
class SkillAdmin(MarkdownxModelAdmin):
    """Display settings for the Skill model on the Admin page"""

    list_display = ('title', 'id')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    """Display settings for the Resume model on the Admin page"""

    list_display = ('id', )


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

    list_display = ('id', )


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

    list_display = ('id', )

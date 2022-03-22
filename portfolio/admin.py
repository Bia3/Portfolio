from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import CurriculumVitae, Resume, Project, Skill, WorkExperience, \
    Education, Responsibility, Course, CourseWork, Achievement


def year_from_date(date):
    return date.year


def start_year(obj):
    return year_from_date(obj.start)


def end_year(obj):
    return year_from_date(obj.end)


def completed_year(obj):
    return year_from_date(obj.completed)


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
    if ach.work_experience:
        return username_from_work_experience(ach.work_experience)
    if ach.education:
        return username_from_education(ach.education)
    return 'None'


def username_from_course(cor):
    if cor.education:
        return username_from_education(cor.education)
    return 'None'


def username_from_course_work(cw):
    if cw.course:
        return username_from_course(cw.course)
    return 'None'


def username_from_responsibility(res):
    if res.work_experience:
        return username_from_work_experience(res.work_experience)
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

    list_display = ('view_summary', 'view_username', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        return username_from_cv(obj)

    @staticmethod
    @admin.display(description='summary')
    def view_summary(obj):
        return obj.summary[0:20]


@admin.register(Responsibility)
class ResponsibilityAdmin(MarkdownxModelAdmin):
    """Display settings for the Responsibility model on the Admin page"""

    list_display = ('title', 'view_organization',
                    'view_position', 'view_username', 'id')

    @staticmethod
    def view_position(obj):
        return obj.work_experience.position

    @staticmethod
    def view_organization(obj):
        return obj.work_experience.organization

    @staticmethod
    def view_username(obj):
        return username_from_responsibility(obj)


@admin.register(WorkExperience)
class WorkExperienceAdmin(MarkdownxModelAdmin):
    """Display settings for the WorkExperience model on the Admin page"""

    list_display = ('view_username', 'organization',
                    'position', 'start', 'end', 'id')

    @staticmethod
    def view_username(obj):
        return username_from_work_experience(obj)


@admin.register(Education)
class EducationAdmin(MarkdownxModelAdmin):
    """Display settings for the Education model on the Admin page"""

    list_display = ('degree', 'institution', 'view_username',
                    'view_start_year', 'view_end_year', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        return username_from_work_experience(obj)

    @staticmethod
    @admin.display(description="start")
    def view_start_year(obj):
        return start_year(obj)

    @staticmethod
    @admin.display(description="end")
    def view_end_year(obj):
        return end_year(obj)


@admin.register(Course)
class CourseAdmin(MarkdownxModelAdmin):
    """Display settings for the Course model on the Admin page"""

    list_display = ('id', )

    @staticmethod
    def view_username(obj):
        return username_from_course(obj)


@admin.register(CourseWork)
class CourseWorkAdmin(MarkdownxModelAdmin):
    """Display settings for the CourseWork model on the Admin page"""

    list_display = ('id', )

    @staticmethod
    def view_username(obj):
        return username_from_course_work(obj)


@admin.register(Project)
class ProjectAdmin(MarkdownxModelAdmin):
    """Display settings for the Project model on the Admin page"""

    list_display = ('id', )

    @staticmethod
    def view_username(obj):
        return username_from_project(obj)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    """Display settings for the Achievement model on the Admin Page"""

    list_display = ('title', 'view_username', 'completed', 'id')

    @staticmethod
    def view_username(obj):
        return username_from_achievement(obj)

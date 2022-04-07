from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import CurriculumVitae, Resume, Project, Skill, WorkExperience, \
    Education, Responsibility, Course, CourseWork, Achievement


def year_from_date(date):
    """:return: the year for a date object"""
    return date.year


def start_year(obj):
    """:return: the year for start"""
    return year_from_date(obj.start)


def end_year(obj):
    """:return: the year for end"""
    return year_from_date(obj.end)


def completed_year(obj):
    """:return: the year for completed"""
    return year_from_date(obj.completed)


def username_from_project(proj):
    """:return: the username for a project"""
    return proj.user.username


def username_from_resume(res):
    """:return: the username for a resume"""
    return res.user.username


def username_from_cv(cv):
    """:return: the username for a cv"""
    return cv.user.username


def username_from_work_experience(we):
    """:return: the username for a work experience"""
    if we.resume:
        return username_from_resume(we.resume)
    if we.project:
        return username_from_project(we.project)
    if we.cv:
        return username_from_cv(we.cv)
    return 'None'


def username_from_education(ed):
    """:return: the username for a user from the education field"""
    if ed.resume:
        return username_from_resume(ed.resume)
    if ed.cv:
        return username_from_cv(ed.cv)
    return 'None'


def username_from_skill(sk):
    """:return: the username for a user from the skill field"""
    if sk.project:
        return username_from_project(sk.project)
    if sk.resume:
        return username_from_resume(sk.resume)
    if sk.cv:
        return username_from_cv(sk.cv)
    return 'None'


def username_from_achievement(ach):
    """:return: the username for a user from the achievement field"""
    if ach.project:
        return username_from_project(ach.project)
    if ach.work_experience:
        return username_from_work_experience(ach.work_experience)
    if ach.education:
        return username_from_education(ach.education)
    return 'None'


def username_from_course(cor):
    """:return: the username for a user from the course field"""
    if cor.education:
        return username_from_education(cor.education)
    return 'None'


def username_from_course_work(cw):
    """:return: the username for a user from the course work field"""
    if cw.course:
        return username_from_course(cw.course)
    return 'None'


def username_from_responsibility(res):
    """:return: the username for a user from the responsibility field"""
    if res.work_experience:
        return username_from_work_experience(res.work_experience)
    return 'None'


@admin.register(Skill)
class SkillAdmin(MarkdownxModelAdmin):
    """Settings for the Skill model on the Admin page"""

    list_display = ('title', 'view_username', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        """:return: the username for this object"""
        return username_from_skill(obj)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    """Settings for the Resume model on the Admin page"""

    list_display = ('view_username', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        """:return: the username for this object"""
        return username_from_resume(obj)


@admin.register(CurriculumVitae)
class CurriculumVitaeAdmin(admin.ModelAdmin):
    """Settings for the CurriculumVitae model on the Admin page"""

    list_display = ('view_summary', 'view_username', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        """:return: the username for this object"""
        return username_from_cv(obj)

    @staticmethod
    @admin.display(description='summary')
    def view_summary(obj):
        """:return: the first 20 characters from the summary field"""
        return obj.summary[0:21]


@admin.register(Responsibility)
class ResponsibilityAdmin(MarkdownxModelAdmin):
    """Settings for the Responsibility model on the Admin page"""

    list_display = ('title', 'view_organization',
                    'view_position', 'view_username', 'id')

    @staticmethod
    @admin.display(description='position')
    def view_position(obj):
        """:return: the position from the work experience object"""
        return obj.work_experience.position

    @staticmethod
    @admin.display(description='organization')
    def view_organization(obj):
        """:return: the organization from the work experience object"""
        return obj.work_experience.organization

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        """:return: the username for this object"""
        return username_from_responsibility(obj)


@admin.register(WorkExperience)
class WorkExperienceAdmin(MarkdownxModelAdmin):
    """Settings for the WorkExperience model on the Admin page"""

    list_display = ('view_username', 'organization',
                    'position', 'start', 'end', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        """:return: the username for this object"""
        return username_from_work_experience(obj)


@admin.register(Education)
class EducationAdmin(MarkdownxModelAdmin):
    """Settings for the Education model on the Admin page"""

    list_display = ('degree', 'institution', 'view_username',
                    'view_start_year', 'view_end_year', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        """:return: the username for this object"""
        return username_from_work_experience(obj)

    @staticmethod
    @admin.display(description="start")
    def view_start_year(obj):
        """:return: return the year for the start field"""
        return start_year(obj)

    @staticmethod
    @admin.display(description="end")
    def view_end_year(obj):
        """:return: return the year for the end field"""
        return end_year(obj)


@admin.register(Course)
class CourseAdmin(MarkdownxModelAdmin):
    """Settings for the Course model on the Admin page"""

    list_display = ('id', )

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        """:return: the username for this object"""
        return username_from_course(obj)


@admin.register(CourseWork)
class CourseWorkAdmin(MarkdownxModelAdmin):
    """Settings for the CourseWork model on the Admin page"""

    list_display = ('id', )

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        """:return: the username for this object"""
        return username_from_course_work(obj)


@admin.register(Project)
class ProjectAdmin(MarkdownxModelAdmin):
    """Settings for the Project model on the Admin page"""

    list_display = ('title', 'view_username', 'view_completed_year', 'id', )

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        """:return: the username for this object"""
        return username_from_project(obj)

    @staticmethod
    @admin.display(description='completed')
    def view_completed_year(obj):
        """:return: the year from the completed field"""
        return completed_year(obj)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    """Settings for the Achievement model on the Admin Page"""

    list_display = ('title', 'view_username',
                    'view_category', 'completed', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        """:return: the username for this object"""
        return username_from_achievement(obj)

    @staticmethod
    @admin.display(description='category')
    def view_category(obj):
        """:return: the category for this object"""
        if obj.work_experience:
            return 'Work Experience'
        if obj.course_work:
            return 'Course Work'
        if obj.education:
            if obj.education.certificate:
                return 'Certificate'
        if obj.project:
            if obj.project.field_experience:
                return 'Project - Field Experience'
            if obj.project.professional_development:
                return 'Project - Professional Development'
        return 'None'

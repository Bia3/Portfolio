from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Job, CurriculumVitae, Resume, Project, Skill, Bio,\
    Responsibility, Section, ContactCard, School, Accomplishment, Certificate, \
    File, CodeSnippet, ProjectSection, Svg, Achievement


@admin.register(Svg)
class SvgAdmin(admin.ModelAdmin):
    """
    Display settings for the Svg model on the Admin page
    """
    list_display = ('name', )
    fieldsets = [
        (None, {'fields': ['name', 'data']}),
    ]


@admin.register(Skill)
class SkillAdmin(MarkdownxModelAdmin):
    """
    Display settings for the Skill model on the Admin page
    """
    list_display = ('name', )


admin.site.register(Responsibility, MarkdownxModelAdmin)
admin.site.register(Accomplishment, MarkdownxModelAdmin)
admin.site.register(Job, MarkdownxModelAdmin)
admin.site.register(School, MarkdownxModelAdmin)
admin.site.register(Section, MarkdownxModelAdmin)
admin.site.register(Certificate, MarkdownxModelAdmin)
admin.site.register(Resume, MarkdownxModelAdmin)
admin.site.register(File)
admin.site.register(CodeSnippet)
admin.site.register(ProjectSection)
admin.site.register(Project, MarkdownxModelAdmin)
admin.site.register(CurriculumVitae, MarkdownxModelAdmin)
admin.site.register(Bio, MarkdownxModelAdmin)
admin.site.register(ContactCard)
admin.site.register(Achievement)

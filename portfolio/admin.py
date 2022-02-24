from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Job, CurriculumVitae, Resume, Project, Skill, Bio,\
    Responsibility, Section, ContactCard, School, Accomplishment, Certificate, \
    File, CodeSnippet, ProjectSection, Svg, Achievement


class SvgAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fieldsets = [
        (None, {'fields': ['name', 'data']}),
    ]


class SkillAdmin(MarkdownxModelAdmin):
    list_display = ('name', )


admin.site.register(Skill, SkillAdmin)
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
admin.site.register(Svg, SvgAdmin),
admin.site.register(Achievement)
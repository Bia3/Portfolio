from django import forms
from .models import Achievement
from markdownx.fields import MarkdownxFormField


class AchievementForm(forms.ModelForm):
    """Form to create or update Achievement records"""

    class Meta:
        """Meta Class to set up the Achievements Form"""

        model = Achievement
        fields = ['title', 'summary', 'copy']


class SkillForm(forms.Form):
    """Form to create or update Skill records"""

    title = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "name_field"})
    )
    summary = forms.CharField(
        label='Description',
        max_length=4000,
        widget=forms.Textarea(attrs={'class': "description_area"})
    )
    copy = MarkdownxFormField(
        label='Copy',
        max_length=4000,
        widget=forms.Textarea(attrs={'class': "highlights_area"})
    )


class ProjectForm(forms.Form):
    """Form to create or update Project records"""

    title = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "name_field"})
    )
    short_summary = forms.CharField(
        label='Description',
        max_length=4000,
        widget=forms.Textarea(attrs={'class': "short_description_area"})
    )
    github_link = forms.CharField(
        label='Git Hub Link',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "git_link_field"})
    )

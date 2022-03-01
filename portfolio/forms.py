from django import forms
from .models import Achievement


class AchievementForm(forms.ModelForm):
    """
    Form to create or update Achievement records
    """
    class Meta:
        """
        Meta Class to set up the Achievements Form
        """
        model = Achievement
        fields = ['name', 'description', 'order']


class SkillForm(forms.Form):
    """
    Form to create or update Skill records
    """
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "name_field"})
    )
    description = forms.CharField(
        label='Description',
        max_length=4000,
        widget=forms.Textarea(attrs={'class': "description_area"})
    )
    highlights = forms.CharField(
        label='Highlights',
        max_length=4000,
        widget=forms.Textarea(attrs={'class': "highlights_area"})
    )


class ProjectForm(forms.Form):
    """
    Form to create or update Project records
    """
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "name_field"})
    )
    short_desc = forms.CharField(
        label='Description',
        max_length=4000,
        widget=forms.Textarea(attrs={'class': "short_description_area"})
    )
    git_link = forms.CharField(
        label='Git Hub Link',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "git_link_field"})
    )

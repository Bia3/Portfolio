from django import forms
from RossDevs.models import Achievement, Skill


class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['name', 'description', 'order']


class SkillForm(forms.Form):
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

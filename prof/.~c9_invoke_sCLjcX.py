from django import forms
from django.forms import ModelForm
from prof.models import FileSpace



class FileSpaceForm(forms.ModelForm):
    class Meta:
        model = FileSpace
        fields = ['FileType', 'Name', 'File','Description']
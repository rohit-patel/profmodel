from django import forms
from django.forms import ModelForm
from prof.models import FileSpace



class FileSpaceForm(forms.ModelForm):
    class Meta:
        model = FileSpace
        fields = ['FileType', 'FileName', 'TheActualFile','FileDescription']

class UploadForm(forms.Form):
    
    docfile = forms.FileField(
        label='Select a file',
        help_text='Use Template Provided'
    )
    
class userfield(forms.Form):
    username = forms.CharField(label='Username',max_length=20)

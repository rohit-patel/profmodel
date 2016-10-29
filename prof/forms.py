from django import forms

class UploadForm(forms.Form):
    
    docfile = forms.FileField(
        label='Select a file',
        help_text='Use Template Provided'
    )
    
class userfield(forms.Form):
    username = forms.CharField(label='Username',max_length=20)

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

PossibleFileTypes = (('P','P&L File'),('K', 'Key File'),('S', 'Sales Data File'))
    
class FileSpace(models.Model):
    #Owner = models.ForeignKey(User, editable=False)
    CompanyName = models.CharField(max_length=100)
    RunNo = models.IntegerField()
    RunName = models.CharField(max_length=20)
    Filetype = models.CharField(max_length=1,choices=PossibleFileTypes)
    TheActualFile = models.FileField()
    
    class Meta:
        permissions = (
            ('file_owner', 'File Owner'), 
            ('file_edit', 'File Edit Permission'), 
        )
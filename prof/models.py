from django.db import models

# Create your models here.

class Project(models.Model):
    user = models.CharField(max_length=20)
    pnlfile = models.FileField()
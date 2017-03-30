from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class RunSpace(models.Model):
    """This is the model that stores IDs for the runs. Basically, all the files and data is mapped to the runs and this model has the primary run ID. 
    """
    CompanyName = models.CharField(max_length=100, blank=False)
    RunNo = models.IntegerField(blank=False)
    RunName = models.CharField(max_length=20,blank=False)
    RunDescription = models.TextField(blank=True)
    class Meta:
        permissions = (
            ('run_owner', 'File Owner'), 
            ('run_edit_permission', 'File Editing Permission'), 
            ('run_view_permission', 'File Viewing Permission'), 
        )    

    
class FileSpace(models.Model):
    """These are the files uploaded by the user. Each file is mapped to a run and has user permissions that need to be managed.
    """
    Possibletypes = (('P','P&L File'),('K', 'Key File'),('S', 'Sales Data File'))
    #Owner = models.ForeignKey(User, editable=False)
    run = models.ForeignKey(RunSpace,on_delete=models.CASCADE)
    #CompanyName = models.CharField(max_length=100, blank=False)
    #RunNo = models.IntegerField(blank=False)
    #RunName = models.CharField(max_length=20,blank=True)
    FileType = models.CharField(max_length=1,choices=Possibletypes,blank=False,default='K')
    FileName = models.CharField(max_length=20,blank=False)
    File = models.FileField(blank=False)
    FileDescription = models.TextField(blank=True)
    class Meta:
        permissions = (
            ('file_owner', 'File Owner'), 
            ('file_edit_permission', 'File Editing Permission'), 
            ('file_view_permission', 'File Viewing Permission'), 
        )    
    
    
class TransactionData(models.Model):
    run = models.ForeignKey(RunSpace,on_delete=models.CASCADE)
    SourceFile = models.ForeignKey(FileSpace,on_delete=models.CASCADE)
    TransactionNumber = models.CharField(max_length=25,blank=False)
    TransactionDate = models.DateField(blank=False)
    Department = models.CharField(max_length=100,blank=False)
    CustomerNumber = models.CharField(max_length=25,blank=False)
    CustomerName = models.CharField(max_length=100,blank=True)
    ProductNumber = models.CharField(max_length=25,blank=False)
    Quantity = models.IntegerField(blank=False)
    ListPrice = models.FloatField(blank=False)
    TotalPrice = models.FloatField(blank=False)
    Discount = models.FloatField(blank=False)
    InvoiceAmount = models.FloatField(blank=False)
    
    

from django.contrib import admin
from .models import RunSpace, FileSpace, TransactionData, PnLData

# Register your models here.
admin.site.register(RunSpace)
admin.site.register(FileSpace)
admin.site.register(TransactionData)
admin.site.register(PnLData)

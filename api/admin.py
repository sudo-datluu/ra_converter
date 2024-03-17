from django.contrib import admin
from .models import FileUpload, ColumnType, Column
# Register your models here.

admin.site.register(FileUpload)
admin.site.register(ColumnType)
admin.site.register(Column)
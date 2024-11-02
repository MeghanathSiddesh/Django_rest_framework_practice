from django.contrib import admin
from rest1.models import *
# Register your models here.
admin.site.register(StudentModels)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','usn','address','date']
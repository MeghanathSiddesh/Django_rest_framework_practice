from django.contrib import admin

# Register your models here.
from apiview.models import Student
admin.site.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll','city']
from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=25)
    roll=models.IntegerField()
    email=models.EmailField()
    marks=models.IntegerField()
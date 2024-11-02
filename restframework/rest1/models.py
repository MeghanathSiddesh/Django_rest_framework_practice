from django.db import models

# Create your models here.
class StudentModels(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    usn=models.CharField(max_length=20)
    address=models.TextField()
    date=models.DateField(null=True,blank=True)
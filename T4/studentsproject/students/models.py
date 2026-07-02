from django.db import models

# Create your models here.

class Student (models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    enrollment_number = models.IntegerField(unique=True,default=0)
    phn_number = models.IntegerField(default=0)


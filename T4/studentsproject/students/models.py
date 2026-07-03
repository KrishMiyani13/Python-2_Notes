from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.name} ({self.code})'
    
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    enrollment_number = models.IntegerField(unique=True,default=0)
    phn_number = models.IntegerField(default=0)
    course = models.ManyToManyField(Course)
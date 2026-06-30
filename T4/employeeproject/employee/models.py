from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=50)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    salary = models.IntegerField()
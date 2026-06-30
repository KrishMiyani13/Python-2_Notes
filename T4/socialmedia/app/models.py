from django.db import models

# Create your models here.
class App(models.Model):
    user_name = models.CharField(max_length=50,unique=True)
    post = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    description = models.TextField()
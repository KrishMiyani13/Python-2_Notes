from django.db import models

# Create your models here.
class Music(models.Model):
    song = models.CharField(max_length=225)
    artist = models.CharField(max_length=225)
    year = models.IntegerField()
    album = models.CharField(max_length=225)

    
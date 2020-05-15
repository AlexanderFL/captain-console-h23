from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateField()
    short = models.CharField(max_length=256)
    article = models.TextField(blank=True)
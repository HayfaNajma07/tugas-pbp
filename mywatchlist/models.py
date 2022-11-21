from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    watched = models.BooleanField(default=False)
    rating = models.IntegerField()
    review = models.TextField()
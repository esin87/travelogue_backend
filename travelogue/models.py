from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    photo_url = models.CharField(max_length=200)
    place_name = models.CharField(max_length=100)
    notes = models.TextField()
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name="entries")

    def __str__(self):
        return self.title

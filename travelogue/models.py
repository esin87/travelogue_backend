from django.db import models

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    photo_url = models.CharField(max_length=200)
    place_name = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return self.title

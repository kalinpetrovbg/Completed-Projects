from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    distance = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img_url = models.URLField(null=True, blank=True)

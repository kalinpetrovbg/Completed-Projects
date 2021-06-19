from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    distance = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img_url = models.URLField(null=True, blank=True)
    visited = models.BooleanField(default=False)

    YESORNO = [('yes', 'Yes'), ('no', 'No'), ('Maybe', 'Maybe')]
    # first is hot it is visible in frontend, second is how it is visible on admin.
    choice_dropdown = models.CharField(choices=YESORNO, max_length=10, default='no')



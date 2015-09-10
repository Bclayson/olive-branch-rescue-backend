from django.db import models

__author__ = 'administrator'


class TrackedModel(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

from django.db import models

# Create your models here.
from core.models import TimeStampedModel

class Result(TimeStampedModel):
    """ Test Type Model """
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('name',)

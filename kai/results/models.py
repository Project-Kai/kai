from django.db import models

# Create your models here.
from core.models import TimeStampedModel

class Result(TimeStampedModel):
    """ Test Type Model """
    name = models.CharField(max_length=25)
    file = models.FileField(null=True, upload_to='uploads/%Y/%m/%d/')


    class Meta:
        ordering = ('name',)

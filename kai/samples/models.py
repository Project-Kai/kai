from django.db import models
from datetime import datetime

# Create your models here.
from core.models import TimeStampedModel
from clients.models import Client

class Sample(TimeStampedModel):
    """ Sample Model """
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True, default='')
    sample_date = models.DateTimeField(default=datetime.now)
    sample_point = models.CharField(max_length=50, blank=True, default='')

    water_source = models.CharField(max_length=50, blank=True, default='')
    water_application = models.CharField(max_length=50, blank=True, default='')

    drinking = models.BooleanField(default=False)
    labelled = models.BooleanField(default=False)

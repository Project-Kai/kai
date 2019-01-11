from django.db import models
from datetime import datetime

# Create your models here.
from core.models import TimeStampedModel, WaterSource, WaterApplication
from clients.models import Client

class Sample(TimeStampedModel):
    """ Sample Model """
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)

    location = models.CharField(max_length=50, blank=True, default='')
    sample_date = models.DateTimeField(default=datetime.now)
    sample_point = models.CharField(max_length=50, blank=True, default='')

    drinking = models.BooleanField(default=False)
    labelled = models.BooleanField(default=False)
    response = models.ForeignKey('SampleResponse', on_delete=models.CASCADE, null=True)

    sample_form = models.FileField(null=True, upload_to='uploads/sample/%Y/%m/%d/')

class SampleWaterSource(TimeStampedModel):
    sample = models.ForeignKey('Sample', on_delete=models.CASCADE)
    water_source = models.ForeignKey('core.WaterSource', on_delete=models.CASCADE)

class SampleWaterApplication(TimeStampedModel):
    sample = models.ForeignKey('Sample', on_delete=models.CASCADE)
    water_application = models.ForeignKey('core.WaterApplication', on_delete=models.CASCADE)

class SampleResponse(TimeStampedModel):
    """ Response Model """
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

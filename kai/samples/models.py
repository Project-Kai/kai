from django.db import models
from datetime import datetime

# Create your models here.
from core.models import TimeStampedModel, WaterSource, WaterApplication, Response
from clients.models import Client

class Sample(TimeStampedModel):
    """ Sample Model """
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)

    location = models.CharField(max_length=50, blank=True, default='')
    sample_date = models.DateTimeField(default=datetime.now)
    sample_point = models.CharField(max_length=50, blank=True, default='')

    drinking = models.BooleanField(default=False)
    labelled = models.BooleanField(default=False)

    sample_form = models.FileField(null=True, upload_to='uploads/sample/%Y/%m/%d/')

    class Meta:
        ordering = ('id',)

class SampleWaterSource(TimeStampedModel):
    sample = models.ForeignKey('Sample', on_delete=models.CASCADE)
    water_source = models.ForeignKey('core.WaterSource', on_delete=models.CASCADE)

    class Meta:
        ordering = ('sample__id','water_source__id',)

class SampleWaterApplication(TimeStampedModel):
    sample = models.ForeignKey('Sample', on_delete=models.CASCADE)
    water_application = models.ForeignKey('core.WaterApplication', on_delete=models.CASCADE)

    class Meta:
        ordering = ('sample__id','water_application__id',)

class SampleResponse(TimeStampedModel):
    """ Sample Response Model """
    sample = models.ForeignKey('Sample', on_delete=models.CASCADE)
    response = models.ForeignKey('core.Response', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('sample__id','response__id',)

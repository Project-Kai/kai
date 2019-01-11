from django.db import models

# Create your models here.
from core.models import TimeStampedModel
from samples.models import Sample
from results.models import Result

class Test(TimeStampedModel):
    """ Test Model """
    sample = models.ForeignKey('samples.Sample', on_delete=models.CASCADE)
    test_type = models.ForeignKey('TestType', on_delete=models.CASCADE)
    result = models.ForeignKey('results.Result', on_delete=models.CASCADE)


class TestType(TimeStampedModel):
    """ Test Type Model """
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('name',)

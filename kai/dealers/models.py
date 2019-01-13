from django.db import models

# Create your models here.
from core.models import TimeStampedModel

class Dealer(TimeStampedModel):
    """ Dealer Model """
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=50, blank=True, default='')
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()

    class Meta:
        ordering = ('name',)

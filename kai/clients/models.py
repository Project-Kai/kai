from django.db import models

# Create your models here.
from core.models import TimeStampedModel
from dealers.models import Dealer

class Client(TimeStampedModel):
    """ Client Model """
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=50, blank=True, default='')
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    dealer =  models.ForeignKey('dealers.Dealer', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

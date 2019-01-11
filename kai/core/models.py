from django.db import models

# Create your models here.
from django.utils import timezone
import uuid as uuidlib

class TimeStampedModelManager(models.Manager):

    def save(self, **kwargs):
        kwargs['updated_date'] = timezone.now()
        return super().save(**kwargs)

class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(db_index=True, default=uuidlib.uuid4, editable=False)

    objects = TimeStampedModelManager()

    class Meta:
        abstract = True

class WaterSource(TimeStampedModel):
    """ Water Source Model """
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class WaterApplication(TimeStampedModel):
    """ Water Application Model """
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Response(TimeStampedModel):
    """ Response Model """
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

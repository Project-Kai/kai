from django.contrib import admin

# Register your models here.
from samples.models import Sample, SampleWaterSource, SampleWaterApplication, SampleResponse

admin.site.register(Sample)
admin.site.register(SampleWaterSource)
admin.site.register(SampleWaterApplication)
admin.site.register(SampleResponse)

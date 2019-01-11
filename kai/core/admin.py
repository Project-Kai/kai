from django.contrib import admin

# Register your models here.
from core.models import WaterSource, WaterApplication, Response

admin.site.register(WaterSource)
admin.site.register(WaterApplication)
admin.site.register(Response)

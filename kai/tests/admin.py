from django.contrib import admin

# Register your models here.
from tests.models import Test, TestType

admin.site.register(Test)
admin.site.register(TestType)

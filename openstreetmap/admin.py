from django.contrib import admin
from .models import MyOsm


@admin.register(MyOsm)
class MyOsmAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import MyOsm


class MyOsmAdmin(admin.ModelAdmin):
    pass


admin.site.register(MyOsm, MyOsmAdmin)

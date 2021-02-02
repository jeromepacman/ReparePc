from django.contrib import admin
from .models import MyOsm, Customer


class MyOsmAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date', 'center')


admin.site.register(MyOsm, MyOsmAdmin)
admin.site.register(Customer, CustomerAdmin)

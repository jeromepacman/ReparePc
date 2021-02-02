from django.db import models
from osm_field.fields import LatitudeField, LongitudeField, OSMField


class MyOsm(models.Model):
    location=OSMField("Location (address, zipcode city)")
    email=models.EmailField(blank=True)
    phone=models.IntegerField(null=True, blank=True)
    location_lat=LatitudeField()
    location_lon=LongitudeField()

    def __str__(self):
        return self.location


class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    date=models.DateField(auto_now_add=True)
    center=models.ForeignKey(MyOsm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

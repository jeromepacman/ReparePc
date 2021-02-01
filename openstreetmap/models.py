from django.db import models
from osm_field.fields import LatitudeField, LongitudeField, OSMField


class MyOsm(models.Model):
    location=OSMField()
    address=models.CharField(max_length=100, blank=True)
    zipcode=models.CharField(max_length=5, null=True, blank=True)
    email=models.EmailField(blank=True)
    phone=models.IntegerField(null=True, blank=True)
    location_lat=LatitudeField()
    location_lon=LongitudeField()

    def __str__(self):
        return self.location

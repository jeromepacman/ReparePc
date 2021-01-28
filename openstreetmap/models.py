from django.db import models
from osm_field.fields import LatitudeField, LongitudeField, OSMField


class MyOsm(models.Model):
    titre = models.CharField(max_length=50)
    location=OSMField()
    location_lat=LatitudeField()
    location_lon=LongitudeField()

    def __str__(self):
        return self.location


        
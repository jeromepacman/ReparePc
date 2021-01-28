from django import forms
from .models import MyOsm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


class MyOsmForm(forms.ModelForm):
    class Meta:
        fields=('location', 'location_lat', 'location_lon',)
        model=MyOsm


class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)


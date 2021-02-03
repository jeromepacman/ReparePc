from django import forms
from .models import MyOsm, Customer


class MyOsmForm(forms.ModelForm):
    class Meta:
        model=MyOsm
        fields = '__all__'


class ContactForm(forms.ModelForm):

    class Meta:
        model=Customer
        fields = '__all__'


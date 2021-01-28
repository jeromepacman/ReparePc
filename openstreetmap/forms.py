from django import forms
from .models import MyOsm


class MyOsmForm(forms.ModelForm):
    class Meta:
        model=MyOsm
        fields = '__all__'


class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)


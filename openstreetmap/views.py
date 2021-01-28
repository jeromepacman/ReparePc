from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView, FormView
from .forms import MyOsmForm, ContactForm
from .models import MyOsm


class MyOsmView(CreateView):
    template_name="openstreetmap/myosm_form.html"
    form_class=MyOsmForm
    model=MyOsm

    def get_success_url(self):
        return reverse("index")


class IndexListView(ListView):
    model=MyOsm
    template_name='index.html'


class ContactFormView(FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_url='/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

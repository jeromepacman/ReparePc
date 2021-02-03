from django.conf import settings
from django.shortcuts import reverse
from django.core.mail import send_mail, EmailMessage
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DeleteView, FormView
from django.template.loader import render_to_string
from .forms import MyOsmForm, ContactForm
from .models import MyOsm


class MyOsmView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name="openstreetmap/myosm_form.html"
    form_class=MyOsmForm
    model=MyOsm
    success_message="location added"

    def get_success_url(self):
        return reverse("index")


class MyOsmDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name="openstreetmap/myosm_delete.html"
    model=MyOsm
    success_message="location deleted"
    success_url='/'


class IndexListView(ListView):
    model=MyOsm
    template_name='index.html'


class ContactFormView(SuccessMessageMixin, FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_message='Your message has been sent'
    success_url='/'

    def form_valid(self, form):
        email=form.cleaned_data.get('email')
        subject=form.cleaned_data.get('name')
        message=form.cleaned_data.get('message')
        send_mail(
            subject, message, email, ['contact@onlineformapro.com']
        )
        feedback=render_to_string('confirm.html', {'name': subject})
        email_conf=EmailMessage("Your request is in process", feedback, settings.EMAIL_HOST_USER, [email])
        email_conf.send()
        form.save(commit=True)

        return super(ContactFormView, self).form_valid(form)

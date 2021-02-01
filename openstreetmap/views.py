from django.shortcuts import reverse, render
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, FormView
from .forms import MyOsmForm, ContactForm
from .models import MyOsm


class MyOsmView(SuccessMessageMixin, CreateView):
    template_name="openstreetmap/myosm_form.html"
    form_class=MyOsmForm
    model=MyOsm
    success_message = "location added"

    def get_success_url(self):
        return reverse("index")


class IndexListView(ListView):
    model=MyOsm
    template_name='index.html'


class ContactFormView(SuccessMessageMixin, FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_message = 'Your message has been sent'
    success_url='/'

    def form_valid(self, form):
        email=form.cleaned_data.get('email')
        subject=form.cleaned_data.get('name')
        message=form.cleaned_data.get('message')
        send_mail(
            subject, message, email, ['contact@onlineformapro.com']
        )
        return super(ContactFormView, self).form_valid(form)


def leaf_mapview(request):
    return render(request, 'leafmap.html', {})

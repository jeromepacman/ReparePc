from django.contrib import admin
from django.urls import path
from openstreetmap.views import MyOsmView, IndexListView, ContactFormView


urlpatterns=[
    path('admin/', admin.site.urls),
    path('', IndexListView.as_view(), name='index'),
    path('osm/', MyOsmView.as_view(), name='create'),
    path('contact/', ContactFormView.as_view(), name='contact'),


]



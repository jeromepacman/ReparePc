from django.contrib import admin
from django.urls import path, include
from openstreetmap.views import MyOsmView, IndexListView, ContactFormView, leaf_mapview


urlpatterns=[
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexListView.as_view(), name='index'),
    path('osm/', MyOsmView.as_view(), name='create'),
    path('leafmap/', leaf_mapview, name='leafmap'),
    path('contact/', ContactFormView.as_view(), name='contact'),

]


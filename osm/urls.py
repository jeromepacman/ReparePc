from django.contrib import admin
from django.urls import path, include
from openstreetmap.views import MyOsmView, IndexListView, MyOsmDeleteView,  ContactFormView


urlpatterns=[
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexListView.as_view(), name='index'),
    path('create/', MyOsmView.as_view(), name='create'),
    path('<int:pk>/delete/', MyOsmDeleteView.as_view(), name='delete'),
    path('contact/', ContactFormView.as_view(), name='contact'),

]

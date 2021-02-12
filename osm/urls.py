from django.contrib import admin
from django.urls import path, include
from openstreetmap.views import MyOsmView, IndexListView, MyOsmDeleteView, ContactFormView, CenterMessagesListView, CenterMessagesDetailView


urlpatterns=[
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexListView.as_view(), name='index'),
    path('create/', MyOsmView.as_view(), name='create'),
    path('<int:pk>/delete/', MyOsmDeleteView.as_view(), name='delete'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('<int:pk>/contact/', ContactFormView.as_view(), name='contact'),
    path('messages/', CenterMessagesListView.as_view(), name='messages'),
    path('<int:pk>/message_detail/', CenterMessagesDetailView.as_view(), name='detail')

]

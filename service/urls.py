from django.urls import path
from service.views import index, about

urlpatterns = [
    path('service/', index),
    path('about/<int:id>', about, name='about'),
]
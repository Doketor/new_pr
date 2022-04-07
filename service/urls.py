from django.urls import path
from service.views import index, about, json_show

urlpatterns = [
    path('', index, name ='service'),
    path('about/<int:id>', about, name='about'),
    path('json', json_show, name='json_show'),
]
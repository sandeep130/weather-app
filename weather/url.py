from django.urls import path , include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
]
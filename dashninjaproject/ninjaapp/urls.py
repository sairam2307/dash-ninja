from django.contrib import admin
from ninjaapp.urls import *
from ninjaapp import views
from django.urls import path

urlpatterns = [
    path('', views.tab, name='tab'),
 
   
]
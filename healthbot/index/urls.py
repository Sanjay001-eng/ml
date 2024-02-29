from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('services/predictheart/', views.predictheart, name='predictheart'),
    path('services/predictdiabetes/',
         views.predictdiabetes, name='predictdiabetes'),
    path('services/predictparkinson/',
         views.predictparkinson, name='predictparkinson'),
    path('diabetesresults/', views.diabetesresults, name='diabetesresults'),
    path('heartresults/', views.heartresults, name='heartresults'),
    path('parkinsonresults/', views.parkinsonresults, name='parkinsonresults')
   ]

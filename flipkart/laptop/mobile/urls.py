from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    
    path("samsung/",("views.samsung")),
    path("redmi/",("views.redmi")),


]

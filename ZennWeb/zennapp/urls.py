from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from zennapp import views

urlpatterns = [
    path("",views.home,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='Contact'),
]
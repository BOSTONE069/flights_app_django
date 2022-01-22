from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index") #this is for creating a web app path here

]
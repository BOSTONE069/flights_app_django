from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #this is for creating a web app path here
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")

]
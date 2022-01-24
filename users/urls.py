from django.urls import path

from . import views

urlpatterns = [
    path("", views.index1, name="index1"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")

]
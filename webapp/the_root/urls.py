from django.urls import path
from . import views



urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("detail/", views.detail, name="detail"),
    path("services/", views.service, name="service"),
]

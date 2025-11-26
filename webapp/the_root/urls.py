from django.urls import path # type: ignore
from . import views



urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("detail/<slug:slug>", views.detail, name="detail"),
    path("services/", views.service, name="service"),
    path("profile/", views.profile, name="profile"),
]

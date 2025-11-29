from django.urls import path # type: ignore
from . import views



urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("detail/<slug:slug>", views.detail, name="detail"),
    path("services/", views.service, name="service"),
    path("profile/", views.profile, name="profile"),
    path("all_post/", views.view_all_post, name="all_post"),
    path("create_post/", views.create_post, name="create_post"),
    path("edit_post/<slug:slug>", views.edit_post, name="edit_post"),
]

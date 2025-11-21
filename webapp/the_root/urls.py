from django.urls import path
from . import views


app_name = 'the_root'

urlpatterns = [
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup")
]

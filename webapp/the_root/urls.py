from django.urls import path
from .views import home, signup

app_name = 'the_root'
urlpatterns = [
    path("home/", home, name="home"),
    path("signup/", signup, name="signup")
]

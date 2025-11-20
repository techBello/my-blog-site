from django.urls import path
from .views import home

app_name = 'the_root'
urlpatterns = [
    path("home/", home, name="home")
]

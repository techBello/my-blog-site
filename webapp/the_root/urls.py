from django.urls import path # type: ignore
from . import views
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore





urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("detail/<slug:slug>", views.detail, name="detail"),
    path("services/", views.service, name="service"),
    path("service-detail/<slug:slug>", views.service_detail, name="sservice_detail"),
    path("profile/", views.profile, name="profile"),
    path("all_post/", views.view_all_post, name="all_post"),
    path("create_post/", views.create_post, name="create_post"),
    path("edit_post/<slug:slug>", views.edit_post, name="edit_post"),
    path("like_post/<slug:slug>", views.like_post, name="like_post"),
    path('search/', views.search_posts, name='search'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
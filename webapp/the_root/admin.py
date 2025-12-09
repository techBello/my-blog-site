from django.contrib import admin # type: ignore
from .models import Profile, Post, Comments, Likes, Services, Category, Tag

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Services)
admin.site.register(Category)
admin.site.register(Tag)




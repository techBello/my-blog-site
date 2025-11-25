from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib import messages # type: ignore
from .models import Post, Comments, Likes, Profile

# Create your views here.
def home(request):
    all_posts = Post.objects.all()
    all_comments = Comments.objects.all()
    all_likes = Likes.objects.all()

    return render(request, "base/home.html", {'all_posts':all_posts, 'all_comments':all_comments, 'all_likes':all_likes})

def about(request):
    return render(request, "base/About.html")

def contact(request):
    return render(request, "base/contact.html")

def detail(request, slug):
    post = get_object_or_404(Post, post_slug=slug)
    comments = post.post_comment.all()
    return render(request, "base/detailindex.html", {'post':post, 'comments':comments })

def service(request):
    return render(request, "base/index.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account was successfully created for {username} !')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "base/signup.html", {"form":form})

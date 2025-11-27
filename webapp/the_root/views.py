from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.contrib.auth.forms import UserCreationForm  # type: ignore
from .forms import UserProfileForm
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

def profile(request):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            profile = Profile()  # create object
            profile.user = request.user
            profile.full_name = form.cleaned_data.get("full_name")
            profile.profile_picture = form.cleaned_data.get("profile_picture")
            profile.save()  # save to DB

            # messages.success(request, f'Profile was updated for {name} !')
            return redirect('home')
    else:
        form = UserProfileForm()
    return render(request, "base/profile.html", {"form":form, "user":user})


def view_all_post(request):
    return render(request, "base/all_post.html")

def create_post(request):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            post = Post()  # create object
            post.user = request.user
            post.post_title = form.cleaned_data.get("post_title")
            post.post_img = form.cleaned_data.get("post_img")
            post.post_detail = form.cleaned_data.get("post_detail")
            profile.save()  # save to DB

            # messages.success(request, f'Profile was updated for {name} !')
            return redirect('home')
    else:
        form = UserProfileForm()
    return render(request, "base/create_post.html")


def edit_post(request):
    return render(request, "base/edit_post.html")



# profile = form.save(commit=False)
# profile.user = user
# profile.full_name = form.cleaned_data.get("full_name")
# profile.profile_picture = form.cleaned_data.get("profile_picture")
# print(profile.user, profile.full_name, profile.profile_picture)
# print(profile)
# profile.save()

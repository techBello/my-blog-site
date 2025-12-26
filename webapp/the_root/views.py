from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.contrib.auth.forms import UserCreationForm  # type: ignore
from .forms import UserProfileForm, CreatePostForm, ContactForm
from django.contrib import messages # type: ignore
from .models import Post, Comments, Likes, Profile, Likes
import bleach # type: ignore
from django.db.models import Q # type: ignore
from django.core.mail import send_mail # type: ignore
from django.core.paginator import Paginator # type: ignore


def search_posts(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Post.objects.filter(
            Q(post_title__icontains=query) | Q(post_detail__icontains=query)
        )
    print("Search results:", results)
    return render(request, 'base/search_results.html', {'results': results, 'query': query})



# Create your views here.
def home(request):
    all_posts = Post.objects.all().order_by('-created')
    paginator = Paginator(all_posts, 2)  # Show 5 posts per page
    all_comments = Comments.objects.all()
    all_likes = Likes.objects.filter(like=True)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, "base/home.html", {'all_posts':all_posts, 'all_comments':all_comments, 'all_likes':all_likes, 'page_obj':page_obj})

def about(request):
    return render(request, "base/About.html")


def detail(request, slug):
    post = get_object_or_404(Post, post_slug=slug)
    comments = post.post_comment.all()
    if request.user is not None and request.user.is_authenticated:
        user_liked = Likes.objects.filter(post=post, user=request.user, like=True).exists()
        return render(request, "base/detailindex.html", {'post':post, 'comments':comments, 'user_liked': user_liked })
    else:
        return render(request, "base/detailindex.html", {'post':post, 'comments':comments})


def service(request):
    return render(request, "base/index.html")


def service_detail(request, slug):
    services = get_object_or_404(service, post_slug=slug)
    return render(request, "base/detailindex.html", {'services':services})


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
            full_name = form.cleaned_data.get("full_name")
            profile_picture = form.cleaned_data.get("profile_picture")    
            profile, created = Profile.objects.update_or_create(
            user=user,
            defaults={
                'full_name': full_name,
                'profile_picture': profile_picture,
            })

            if created:
                pass
            else:
                pass


            # messages.success(request, f'Profile was updated for {name} !')
            return redirect('home')
    else:
        form = UserProfileForm()
    return render(request, "base/profile.html", {"form":form, "user":user})


def view_all_post(request):
    user = request.user
    posts = Post.objects.filter(post_owner=user)
    return render(request, "base/all_post.html", {"posts":posts, "user":user})

def create_post(request):
    user = request.user
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            post = Post()  # create object
            post.post_owner = request.user
            post.post_title = form.cleaned_data.get("post_title")
            post.post_img = form.cleaned_data.get("post_img")
            post.post_detail = form.cleaned_data.get("post_detail")
             # Clean the content
            post.post_detail = bleach.clean(
                post.post_detail,
                tags=['p', 'b', 'i', 'u', 'ul', 'ol', 'li', 'a', 'br', 'strong', 'em'],
                attributes={'a': ['href', 'title']},
                strip=True
            )

            post.save()  # save to DB

            # messages.success(request, f'Profile was updated for {name} !')
            return redirect('home')
    else:
        form = CreatePostForm()
    return render(request, "base/create_post.html", {"form":form, "user":user})


def edit_post(request, slug):
    post = get_object_or_404(Post, post_slug=slug)
    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('all_post')
    else:
        form = CreatePostForm(instance=post)
    return render(request, 'base/edit_post.html', {'form': form})
    # return render(request, "base/edit_post.html", {"post":post})

def like_post(request, slug):
    user = request.user
    post = get_object_or_404(Post, post_slug=slug)
    like_obj, created = Likes.objects.get_or_create(user=user, post=post)
    user_liked = Likes.objects.filter(post=post, user=request.user, like=True).exists()


    if not created:
        # If already exists, toggle the like
        like_obj.like = not like_obj.like
        # print("Toggled like to:", like_obj.like)
        like_obj.save()
        return redirect('detail', slug)
    else:
        # New like is already True by default
        pass
    

    return render(request, "base/detailindex.html", {'post':post, 'user_liked': user_liked})

# workiing on this comment function
def comment_post(request, slug):
    user = request.user
    post = get_object_or_404(Post, post_slug=slug)
    comments = post.post_comment.all()

    if request.method == "POST":
        comment = Comments()
        print("post",post)
        comment.user = user
        comment.post = post
        comment.comment = request.POST.get("comment")
        comment.save()
        return redirect('detail', slug)


    return render(request, "base/detailindex.html", {'post':post})


# profile = form.save(commit=False)
# profile.user = user
# profile.full_name = form.cleaned_data.get("full_name")
# profile.profile_picture = form.cleaned_data.get("profile_picture")
# print(profile.user, profile.full_name, profile.profile_picture)
# print(profile)
# profile.save()

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email or save to DB
            send_mail(
                f"Message from {name}",
                message,
                email,
                ['your_email@example.com'],  # Replace with your email
            )
            return redirect('home')  # Redirect after success

    return render(request, 'base/contact.html', {'form': form})
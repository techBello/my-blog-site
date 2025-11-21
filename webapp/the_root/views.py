from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "base/home.html")

def about(request):
    return render(request, "base/About.html")

def contact(request):
    return render(request, "base/contact.html")

def detail(request):
    return render(request, "base/detailindex.html")

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

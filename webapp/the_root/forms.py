from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post
from django.contrib.auth.forms import UserCreationForm

# for creating custom form with custom fields we use this
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['full_name','profile_picture']


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_title','post_img','post_detail']



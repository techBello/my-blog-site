from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore
from .models import Profile, Post
from django.contrib.auth.forms import UserCreationForm # type: ignore
from ckeditor.widgets import CKEditorWidget # type: ignore Optionally if we want to use CKEditor widget in forms


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
    post_detail = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['post_title','post_img','post_detail']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


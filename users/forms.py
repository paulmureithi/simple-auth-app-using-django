from users.models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from .models import Profile

# creating a custom user creation form
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','password1', 'password2']
        

# a profile creation form
class CreateProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'profile_pic', 'country', 'short_bio']
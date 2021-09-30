from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CreateProfileForm


# user registration view

def register_view(request):
    form = CustomUserCreationForm()
   
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('log_in')
        else:
            messages.error(request, 'Error has occured during sign-up.')


    context = {'form':form}
    return render(request, 'users/register.html', context)


# login view

def log_in(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages(request, 'Sorry, username does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect ('create_profile')

        else:
            messages.error(request, 'Sorry. Username or Password is Incorrect!')
            
    return render(request, 'users/login.html')

# logout view

def logout_user(request):
    logout(request)
    return redirect('log_in')

# create profile view

def create_profile(request):
    profile = request.user
    form = CreateProfileForm(instance=profile)

    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('generate_profile')
        else:
            messages.error(request, 'Error creating your profile.')

    context = {'form':form}        
    return render(request, 'users/profile.html', context)


# genrate user card

def generate_profile(request):
    return render(request, 'users/profile_card.html')
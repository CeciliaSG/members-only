from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, UserProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.db import transaction
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import UserProfile
#from django.contrib.auth import get_user_model
from .forms import UpdateUserProfile, UpdateUserForm



# Create your views here.

# Sign-up/register view
@transaction.atomic
def register(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Yeah you are all signed up. Log in and have a look around.')
            auth_login(request, user)
            return redirect('home')
    else:
        user_form = CustomUserForm()
        profile_form = UserProfileForm()
    return render(request, 'core/registration.html', {'user_form': user_form, 'profile_form': profile_form})

# Login view
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'socialaccount/signup.html')

# Logout view
def logout(request):
    logout(request)
    return redirect('home')   
         
# Account view
@login_required
def edit_user_profile(request):
    try:
        user_instance = request.user
        profile_instance = request.user.userprofile
    except UserProfile.DoesNotExist:
        messages.warning(request, "You are a user but don't have a profile. Please create one by filling in the missing fields.")
        return redirect('registration')

    user_form_update = UpdateUserForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.userprofile)
   

    if request.method == 'POST':
            user_form_update = UpdateUserForm(request.POST, instance=request.user)
            profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

    if user_form_update.is_valid() and profile_form.is_valid():
            user_form_update.save()
            profile_form.save()
            messages.success(request, "You've successfully updated your profile")
            return redirect('profile')
    else:
        user_form_update = UpdateUserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'core/profile.html', {'user_form_update': user_form_update, 'profile_form': profile_form})
        
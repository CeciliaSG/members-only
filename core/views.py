from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, UserProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.db import transaction
from .models import UserProfile



# Create your views here.
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
            return redirect('login')
    else:
        user_form = CustomUserForm()
        profile_form = UserProfileForm()
    return render(request, 'core/registration.html', {'user_form': user_form, 'profile_form': profile_form})

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

def logout(request):
    logout(request)
    return redirect('home')   


@login_required
def account(request):
    return render(request, 'core/account.html')  


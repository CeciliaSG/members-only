# Django imports
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

# Third-party imports
from allauth.account.forms import LoginForm
from allauth.account.utils import complete_signup
from allauth.account import app_settings
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from allauth.account.views import SignupView

# Local application imports
from .forms import (CustomUserForm, UserProfileForm,
                    DeleteAccountForm, UpdateUserProfile, UpdateUserForm)
from .models import UserProfile
from content_management.models import SavedPost


# Create your views here.

# Sign-up/register view
@transaction.atomic
def register(request):
    """
    Display the signup form:
    model:`core.UserProfile and User (AllAuth)`.

    **Context**

    ``post``
        An instance of:
        model:`core.UserProfile and core.UserCreation Model`.

    ``CustomUserForm and UpdateuserProfileForm ``
        An instance of :forms:``

    **Template:**

    :template:`core/registration.html`
    """

    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            email = user_form.cleaned_data.get('email')
            username = user_form.cleaned_data.get('username')

            if User.objects.filter(email=email).exists():
                user_form.add_error('email',
                                    'This email is already registered.'
                                    'Please use a different one.')

            elif User.objects.filter(username=username).exists():
                user_form.add_error('username',
                                    'This username is already taken.'
                                    'Please choose a different one.')

            else:
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                complete_signup(request, user,
                                app_settings.EMAIL_VERIFICATION, 'post_list')
                return redirect('account_email_verification_sent')
        else:
            messages.error(request,
                           'Please correct the errors below.')
    else:
        user_form = CustomUserForm()
        profile_form = UserProfileForm()
    return render(request, 'core/registration.html',
                  {'user_form': user_form, 'profile_form': profile_form})


# Login view
def custom_login(request):
    """
    Display the login form.

    **Context**

    ``login form``
        Form for login`.


    **Template:**

    :template:`accounts/login.html`
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,
                            username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,
                           'Invalid username or password.',
                           extra_tags='profile_login')
            profile_messages = [message for message in
                                messages.get_messages(request)
                                if 'profile_login' in message.tags]

    return render(request, 'accounts/login.html')


# Logout view
@login_required
def logout(request):

    """
    Display the login form.

    **Context**

    ``logout form``
        Form for logout`.


    **Template:**

    :template:`accounts/logout.html`
    """
    logout(request)
    return redirect('home')


# Account view
@login_required
def edit_user_profile(request):

    """
    Displays UpdateUserProfile form,
    prepopulates the form and saves
    the updates to the database. Also renders the
    users saved/bookmarked posts.

    **Context**

    ``UpdateUserProfile form``
        An instance of :form:`core.UpdateUserProfile`

     **Template:**

    :template:`core/profile.html`

    """
    try:
        user_instance = request.user
        profile_instance = request.user.userprofile
    except UserProfile.DoesNotExist:
        messages.warning(request,
                         "You are a user but don't have a profile.")
        return redirect('registration')

    user_form_update = UpdateUserForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.userprofile)

    saved_posts = SavedPost.objects.filter(user=request.user)

    if request.method == 'POST':
        user_form_update = UpdateUserForm(
                request.POST, instance=request.user)
        profile_form = UserProfileForm(
                request.POST, instance=request.user.userprofile)

    if user_form_update.is_valid() and profile_form.is_valid():
        user_form_update.save()
        profile_form.save()
        messages.success(request,
                         "You've successfully updated"
                         "your profile", extra_tags='profile_update')
        return redirect('profile')

    profile_messages = [message for message
                        in messages.get_messages(request)
                        if 'profile_update' in message.tags]

    return render(request, 'core/profile.html',
                  {'user_form_update': user_form_update,
                   'profile_form': profile_form,
                   'saved_posts': saved_posts,
                   'profile_messages': profile_messages})


@login_required
def delete_account(request):
    """
    View to delete the authenticated user's account.

    Requires the user to be logged in.
    Displays a form to confirm account deletion.
    On POST request:
    - Validates the form data.
    - Deletes the user account if the form is valid
    and confirmation checkbox is checked.
    - Redirects to 'post_list' upon successful
    account deletion.
    - Displays a success message confirming
    account deletion.

    On GET request:
    - Initializes a DeleteAccountForm instance for
    rendering the delete account form.

    Parameters:
    - request (HttpRequest): The HTTP request object
    containing metadata about the request.

    Returns:
    - HttpResponse: Renders 'core/delete_account.html'
    template with the delete account form.
                   Redirects to 'post_list' upon successful
                   account deletion.

    Usage:
    - Use this view to allow authenticated users to
    delete their own accounts.
    """
    if request.method == 'POST':
        form = DeleteAccountForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm_delete']:
            request.user.delete()
            messages.success(request, 'Your account has been deleted.')
            return redirect('post_list')
    else:
        form = DeleteAccountForm()
        return render(request,
                      'core/delete_account.html', {'form': form})


def resend_verification_email(request):
    """
    View to resend email verification for a user.

    Allows users to request a resend of the verification
    email if they haven't
    verified their email address yet.

    On POST request:
    - Retrieves the email address from the form data.
    - Checks if a user exists with the provided email
    address.
    - Checks if the email address is associated with
    an unverified email address.
    - Sends a verification email to the user if
    conditions are met.
    - Displays success or informational messages based
    on the email verification status.

    On GET request:
    - Renders the 'core/resend_verification.html' template
    for the user to enter their email address.

    Parameters:
    - request (HttpRequest): The HTTP request object containing
    metadata about the request.

    Returns:
    - HttpResponse: Redirects to 'resend_verification_email' on
    POST request after processing the form data.
                   Renders 'core/resend_verification.html'
                   template on GET request.

    Usage:
    - Use this view to allow users to request a resend of
    the verification email for their account.

    Note:
    - Requires proper integration with a user authentication
    and email confirmation system.
    - Displays appropriate error messages if the provided
    email address is not found or is already verified.
    """
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
                email_address = EmailAddress.objects.get(user=user,
                                                         email=email)
                if not email_address.verified:
                    send_email_confirmation(request, user)
                    messages.success(request, "Verification email sent.")
                else:
                    messages.info(request, "This email is already verified.")
            except User.DoesNotExist:
                messages.error(request,
                               "No user found with this email address.")
            except EmailAddress.DoesNotExist:
                messages.error(request,
                               "Email address not found or already verified.")
        else:
            messages.error(request, "Please enter an email address.")

        return redirect('resend_verification_email')
    return render(request, 'core/resend_verification.html')

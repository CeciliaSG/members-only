from django.urls import path
from .views import ( edit_user_profile, register, delete_account, resend_verification_email)


urlpatterns = [
    path('core/', register, name='registration'),
    path('account/', edit_user_profile, name='profile'),
    path('delete-account/', delete_account, name='delete_account'),
    path('resend-verification/', resend_verification_email,
    name='resend_verification_email'),
]

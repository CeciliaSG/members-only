from django.urls import path
from .views import edit_user_profile


urlpatterns = [
path('account/', edit_user_profile, name='profile'),
]
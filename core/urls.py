from django.urls import path
from .views import edit_user_profile, register


urlpatterns = [
path('core/', register, name='registration'),
path('account/', edit_user_profile, name='profile'),
]

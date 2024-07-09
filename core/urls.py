from django.urls import path
from .views import edit_user_profile, register, delete_account


urlpatterns = [
    path('account/', register, name='registration'),
    path('account/', edit_user_profile, name='profile'),
    path('delete-account/', delete_account, name='delete_account'),

]

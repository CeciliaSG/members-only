from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('posts/', post_list, name='post_list'),
]
from django.urls import path
from .views import PostListView, post_detail
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    #path('like_post/', views.like_post, name='like_post'),
    #path('like_post/<int:post_id>/<slug:slug>/', views.like_post, name='like_post'),
]
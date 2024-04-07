from django.urls import path
from .views import PostListView, post_detail
from . import views
from .views import like_post


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('like_post/', like_post, name='like_post'),
]
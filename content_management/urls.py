from django.urls import path
from .views import PostListView, post_detail
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
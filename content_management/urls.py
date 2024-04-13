from django.urls import path
from .views import PostListView, post_detail, tag_filter
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('tag_filter/<str:tag>/', views.tag_filter, name='restaurants_bars'),
    #path('tag_filter/<str:tag>/', views.tag_filter, name='tag_filter'),
    path('post_tag_detail/<str:tag>/', views.post_tag_detail, name='post_tag_detail'),
    #path('tag_filter/<str:tag>/<path:template>/', views.tag_filter, name='tag_filter'),

    #path('like_post/', views.like_post, name='like_post'),
    #path('like_post/<int:post_id>/<slug:slug>/', views.like_post, name='like_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
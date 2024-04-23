from django.urls import path
from .views import post_detail, tag_filter, PostListView, save_post, like_post, PostListByHeadingView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
     path('neighbourhoods/', views.neighbourhoods_list_view, name='neighbourhoods'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    #path('tag_filter/<str:tag>/', views.tag_filter, name='restaurants_bars'),
    path('post_tag_detail/<str:tag>/', views.post_tag_detail, name='post_tag_detail'),
    path('save_post/<int:post_id>/', views.save_post, name='save_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('heading/<str:heading_name>/', PostListByHeadingView.as_view(), name='post_list_by_heading'),
    path('tag_filter/restaurants_bars/<str:tags>/', views.restaurants_bars_view, name='restaurants_bars'),
    path('tag_filter/things_to_do/<str:tags>/', views.things_to_do_view, name='things_to_do'),
    path('tag_filter/whats_on/<str:tags>/', views.whats_on_view, name='whats_on'),
    path('tag_filter/perks/<str:tags>/', views.perks_view, name='perks'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


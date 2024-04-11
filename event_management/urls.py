from django.urls import path
from .views import event_list
from . import views


urlpatterns = [
path('events/', event_list, name='event_list'),
path('<slug:slug>/', views.event_detail, name='event_detail'),
]
from django.urls import path
from .views import event_list, event_detail
from . import views


urlpatterns = [
path('events/', event_list, name='event_list'),
#path('<int:event_id>/', views.event_detail, name='event_detail'),
]
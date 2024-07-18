from django.urls import path
from . import views
from .views import rsvp_event

urlpatterns = [
    path('events/<int:event_id>/', views.rsvp_event, name='event_detail'),
    path('events/<int:event_id>/', views.rsvp_event, name='rsvp_event_detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('events/<int:event_id>/', views.rsvp_event, name='event_detail'),
]
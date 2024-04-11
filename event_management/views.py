from django.shortcuts import render
from .models import Event

# Create your views here

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'events/event_detail.html', {'event': event})
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Event

# Create your views here

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, even_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event, 'event_id': event_id})
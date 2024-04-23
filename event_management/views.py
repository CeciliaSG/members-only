from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Event

# Create your views here

def event_list(request):
    """
    Gets list of event posts/objects 
    and displays to event_list.html.
    """
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    """
    Gets individual event post/object 
    and displays to event_detail.html.
    """
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})



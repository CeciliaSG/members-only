from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event, Heading

# Create your views here

def event_list(request):
    """
    Gets list of event posts/objects 
    and displays to event_list.html.
    """
    print("Event list view accessed")

    events = Event.objects.all()

    print(len(events))
    tags = Event.objects.values_list('tag', flat=True).distinct()

    if 'tags' in request.GET:
        tags_filter = request.GET.getlist('tags')
        events = events.filter(tag__in=tags_filter)

    return render(request, 'events/event_list.html', {'events': events, 'tags': tags})



def event_detail(request, event_id):
    """
    Gets individual event post/object 
    and displays to event_detail.html.
    """
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})



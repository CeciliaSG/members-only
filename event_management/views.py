from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Event, Heading

# Create your views here


def event_list(request):

    """
    Returns all instances of events/objects and displays
    as list :model:`event_management.Event`.

    **Context**
    ``event``
        The most recent instance of :model:`event_management.Event`.

    **Template**
    :template:`events/event_detail.html`

    """

    events = Event.objects.all()

    print(len(events))
    tags = Event.objects.values_list('tag', flat=True).distinct()

    if 'tags' in request.GET:
        tags_filter = request.GET.getlist('tags')
        events = events.filter(tag__in=tags_filter)

    return render(request, 'events/event_list.html', {
            'events': events, 'tags': tags})


def event_detail(request, event_id):
    """
    Returns and individual instance of event and displays
     :model:`event_management.Event`.

    **Context**
    ``event``
        The most recent instance of :model:`event_management.Event`.
    ``form rsvp``

    **Template**
    :template:`events/event_list.html`
    """
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

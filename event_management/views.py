from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Event

# Create your views here

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})


def post_detail(request, slug):

    """
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "content_management/post_detail.html",
        {"post": post},
    )
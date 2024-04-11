from django.shortcuts import render, redirect
from .models import Event
from .forms import RSVPForm

# Create your views here.
def rsvp_event(request, event_id):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            event_id = form.cleaned_data['event_id']
            event = Event.objects.get(pk=event_id)
            if request.user in event.rsvp_users.all():
                event.rsvp_users.remove(request.user)
            else:
                event.rsvp_users.add(request.user)
            return redirect('event_detail', event_id=event_id)
    else:
        form = RSVPForm(initial={'event_id': event_id})

    return render(request, 'event_detail.html', {'form': form, 'event': event})
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Rsvp
from .forms import RsvpForm



# Create your views here.
@login_required
def rsvp_event(request, event_id):
    """
    Lets users RSVP for events.
    """
    event = Event.objects.get(pk=event_id)
    rsvp, created = Rsvp.objects.get_or_create(user=request.user, event=event)

    if request.method == 'POST':
        form = RsvpForm(request.POST)
        if form.is_valid():
            rsvp.response = form.cleaned_data['response']
            rsvp.num_guests = form.cleaned_data['num_guests']
            rsvp.save()
            message = "Thank you for RSVPing to the event!"
            messages.success(request, message)
            return redirect('event_detail', event_id=event_id)
    else:
        form = RsvpForm(initial={'event_id': event_id})

    return render(request, 'events/event_detail.html', {
        'form': form, 'event': event})

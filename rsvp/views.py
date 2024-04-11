from django.shortcuts import render, redirect
from .models import Event, Rsvp
from .forms import RsvpForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def rsvp_event(request, even_id):
    print("Request method:", request.method)  
    print("Event ID:", event_id)  

    event = Event.objects.get(pk=event_id)

def rsvp_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    rsvp, created = Rsvp.objects.get_or_create(user=request.user, event=event)

    if request.method == 'POST':
        form = RsvpForm(request.POST)
        if form.is_valid():
            rsvp.response = form.cleaned_data['response']
            rsvp.num_guests = form.cleaned_data['num_guests']
            rsvp.save()
            return redirect('rsvp_event_detail', event_id=event_id)
    else:
        form = RsvpForm(initial={'event_id': event_id})

    return render(request, 'events/event_detail.html', {'form': form, 'event': event})
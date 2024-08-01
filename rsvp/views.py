from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .models import Event, Rsvp
from .forms import RsvpForm


# Create your views here.

def send_confirmation_email(user, event, rsvp):
    subject = f"RSVP Confirmation for {event.title}"
    message = (
        f"Dear {user.first_name},\n\n"
        f"Thank you for RSVPing to {event.title}.\n"
        f"Your response: {rsvp.response}\n"
        f"Number of guests: {rsvp.num_guests}\n\n"
        f"We look forward to seeing you there!\n\n"
        f"Best regards,\n"
        f"The Spotted Team"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)


@login_required
def rsvp_event(request, event_id):
    """
    Renders the form event rsvp in :model:`.rsvp`,
    and lets uers rsvp.

    **Context**

    ``queryset``
        An instance of :form `rsvp`

    **Template:**

    :template:`events/event_detail.html`
    """

    event = Event.objects.get(pk=event_id)
    rsvp, created = Rsvp.objects.get_or_create(user=request.user, event=event)

    if request.method == 'POST':
        form = RsvpForm(request.POST)
        if form.is_valid():
            rsvp.response = form.cleaned_data['response']
            rsvp.num_guests = form.cleaned_data['num_guests']
            rsvp.save()
            send_confirmation_email(request.user, event, rsvp)

            message = ("Thank you for RSVPing to the event!"
            " You will find an email in your inbox with the details.")
            messages.success(request, message)
            return redirect('event_detail', event_id=event_id)
    else:
        form = RsvpForm(initial={'event_id': event_id})

    return render(request, 'events/event_detail.html', {
        'form': form, 'event': event})

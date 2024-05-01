from django.db import models
from django.contrib.auth.models import User
from event_management.models import Event

# Create your models here.

class Rsvp(models.Model):
    """
    Saves a single RSVP for an event post/entry related to :models:`User and Event`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    response_choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),]

    guest_choices = [
        ('1', '1'),
         ('2', '2'),
          ('3', '3'),
           ('4', '4'),
            ('5', '5'),
    ]    

    response = models.CharField(max_length=5, choices=response_choices)
    num_guests = models.CharField(max_length=10, choices=guest_choices)

from django import forms
from django.contrib.auth.models import User

class RsvpForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput())
    response = forms.ChoiceField(choices=[(
        'Yes', 'Yes, of course I will be there.'),
        ('No', 'No, unfortunately I will not be attending this time.')],
     widget=forms.RadioSelect, label="Let us know:")
    num_guests = forms.ChoiceField(choices=[
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'),
                    ('4', '4'), ('5', '5'), ('6', '6')], required=True,
        label="Bringing a guest. Let us know how many")
from django import forms
from django.contrib.auth.models import User

class RsvpForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput())
    response = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect)
    number_of_guests = forms.ChoiceField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6') ], required=True)
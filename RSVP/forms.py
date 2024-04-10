from django import forms

class RSVPForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput())
    response = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect)
    num_guests = forms.ChoiceField(choices=[('0', '0'), ('1', '1'), ('2', '2')], required=True)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    user_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user_name')

class UserProfileForm(forms.ModelForm):  
    interests = forms.MultipleChoiceField(choices=UserProfile.INTEREST_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
      

    class Meta:
        model = UserProfile
        fields = ['city', 'neighbourhood', 'interests']
    

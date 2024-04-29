from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.PasswordInput)
    confirm_email = forms.EmailField(required=True, label="Confirm Email", widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30, widget=forms.PasswordInput)
    confirm_username = forms.CharField(required=True, label="Confirm Username", widget=forms.PasswordInput)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        if email and confirm_email and email != confirm_email:
            raise forms.ValidationError("Emails do not match.")

        username = cleaned_data.get("username")
        confirm_username = cleaned_data.get("confirm_username")
        if username and confirm_username and username != confirm_username:
            raise forms.ValidationError("Usernames do not match.")

class UserProfileForm(forms.ModelForm):  
    interests = forms.MultipleChoiceField(choices=UserProfile.INTEREST_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
      
    class Meta:
        model = UserProfile
        fields = ['city', 'neighbourhood', 'interests']
    
# Update user form
class UpdateUserProfile(forms.ModelForm):

    city = forms.CharField(max_length=100)
    neighbourhood = forms.CharField(max_length=100)
    interests = forms.MultipleChoiceField(choices=UserProfile.INTEREST_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
            model = UserProfile
            fields = ['city', 'neighbourhood', 'interests']

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super(UpdateUserProfile, self).__init__(*args, **kwargs)

        if instance and instance.user:
                self.fields['email'] = forms.EmailField(initial=instance.user.email, required=True)
                self.fields['username'] = forms.CharField(initial=instance.user.username, max_length=30)
        

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.PasswordInput)
    confirm_email = forms.EmailField(required=True, label="Confirm Email", widget=forms.PasswordInput)
    confirm_username = forms.CharField(required=True, label="Confirm Username", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        if email and confirm_email and email != confirm_email:
            self.add_error('confirm_email', "Emails do not match.")

        username = cleaned_data.get("username")
        confirm_username = cleaned_data.get("confirm_username")
        if username and confirm_username and username != confirm_username:
            self.add_error('confirm_username', "Usernames do not match.")


class DeleteAccountForm(forms.Form):
        confirm_delete = forms.BooleanField(required=True, label='Confirm Account Deletion')



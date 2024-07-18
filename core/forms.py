from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class CustomUserForm(UserCreationForm):

    """
    Form class for users to register/create an account.
    """

    email = forms.EmailField(required=True)
    confirm_email = forms.EmailField(required=True, label="Confirm Email")
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    confirm_username = forms.CharField(required=True, label="Confirm Username")

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

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    interests = forms.MultipleChoiceField(choices=UserProfile.INTEREST_CHOICES,
                                          required=False, widget=forms.
                                          CheckboxSelectMultiple)

    class Meta:
        model = UserProfile
        fields = ['city', 'neighbourhood', 'interests']


# Update user form
class UpdateUserProfile(forms.ModelForm):
    """
    Form class for users to update their profile information.
    """

    city = forms.CharField(max_length=100)
    neighbourhood = forms.CharField(max_length=100)
    interests = forms.MultipleChoiceField(choices=UserProfile.INTEREST_CHOICES,
                                          required=False, widget=forms.
                                          CheckboxSelectMultiple)

    class Meta:
        model = UserProfile
        fields = ['city', 'neighbourhood', 'interests']

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super(UpdateUserProfile, self).__init__(*args, **kwargs)

        if instance and instance.user:
            self.fields['email'] = forms.EmailField(initial=instance.user.
                                                    email, required=True)
            self.fields['username'] = forms.CharField(initial=instance.user.
                                                      username, max_length=30)


class UpdateUserForm(forms.ModelForm):

    """
    Form class for users to update their account information.
    """

    email = forms.EmailField(required=True)
    confirm_email = forms.EmailField(required=True, label="Confirm Email")
    confirm_username = forms.CharField(required=True, label="Confirm Username")

    class Meta:
        model = User
        fields = ['email', 'username']

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        if instance:
            self.fields['email'].initial = instance.email
            self.fields['username'].initial = instance.username

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        username = cleaned_data.get("username")
        confirm_username = cleaned_data.get("confirm_username")

        if email and confirm_email and email != confirm_email:
            self.add_error('confirm_email', "Emails do not match.")

        if username and confirm_username and username != confirm_username:
            self.add_error('confirm_username', "Usernames do not match.")

        if email and User.objects.filter(email=email).exclude(
                pk=self.instance.pk).exists():
            self.add_error('email', "This email is already in use.")

        if username and User.objects.filter(username=username).exclude(
                pk=self.instance.pk).exists():
            self.add_error('username', "This username is already taken.")

        return cleaned_data


class DeleteAccountForm(forms.Form):
    """
    Form class for users to delete their account and all associated information
    """

    confirm_delete = forms.BooleanField(required=True,
                                        label='Confirm Account Deletion')
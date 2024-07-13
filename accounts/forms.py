from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from profiles.models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'website', 'profile_picture', 'skills', 'contact_email', 'phone_number']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

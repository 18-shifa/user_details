from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'website', 'profile_picture', 'skills', 'contact_email', 'phone_number']

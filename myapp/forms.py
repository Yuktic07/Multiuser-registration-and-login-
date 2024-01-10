from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=100, label='Address Line 1')
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    pincode = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password', 'confirm_password', 'address_line1', 'city', 'state', 'pincode']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['is_doctor']

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


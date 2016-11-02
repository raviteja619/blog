from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Username'}))
    email = forms.CharField(
        required=True, widget=forms.EmailInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Email'}))
    password1 = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Password'}))
    password2 = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Password Again'}))
    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'First Name'}))
    last_name = forms.CharField(
        required=False, widget=forms.TextInput(attrs={
            'class': 'bn-input', 'placeholder': 'Last Name'}))

    def save(self, *args, **kwargs):
        super(RegistrationForm, self).save()
        user = User.objects.get(username=kwargs['username'])
        user.first_name = kwargs['first_name']
        user.last_name = kwargs['last_name']
        user.email = kwargs['email']
        user.save()


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Username'}))
    password = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Password'}))

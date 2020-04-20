from django.forms import ModelForm, forms
from django.contrib.auth.forms import UserCreationForm, User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreatePassForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    class Meta:
        model = PasswordAccount
        fields = ['title',
                  'username',
                  'password',
                  'url',
                  'additional_notes']


class UpdatePassForm(ModelForm):
    class Meta:
        model = PasswordAccount
        fields = ['title',
                  'username',
                  'password',
                  'url',
                  'additional_notes']

# class CreatePassForm(forms.Form):
#     title = forms.CharField(label='Title')
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     url = forms.URLField()
#     additional_notes = forms.CharField(widget=forms.Textarea)
    
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user import models as usmodels
from twitter import models


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,label='Name')
    email = forms.EmailField(max_length=254,required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2',)


class TwitForm(forms.ModelForm):
    class Meta:
        model = models.Twit
        fields = ['title', 'text']


class PicForm(forms.ModelForm):
    class Meta:
        model = usmodels.Profile
        fields = ['pic']

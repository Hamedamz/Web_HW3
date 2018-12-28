from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user import models as usmodels
from twitter import models
from django.contrib.auth import authenticate


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Name')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

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


class SignInForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def init(self, *args, **kwargs):
        super(SignInForm, self).init(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].initial = ""
        self.fields.keyOrder = [
            'username', 'password'
        ]

    def clean(self):
        cd = super(SignInForm, self).clean()
        password = cd.get('password')
        username = cd.get('username')
        try:
            username = username.lower()
        except AttributeError:
            pass
        if username:
            user = authenticate(username=username, password=password)
            if user is not None:
                if not user.is_active:
                    self.errors['username'] = u"Your account is not activate."
                    return
                self.user = user
            else:
                self.errors['password'] = u'Incorrect username or password.'
                return

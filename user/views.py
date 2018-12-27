from django.urls import reverse_lazy
from django.views import generic
from website import forms


class SignUp(generic.CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'user/signup.html'

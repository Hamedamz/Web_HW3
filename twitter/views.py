from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Twit
from django.urls import reverse_lazy
from django.views import generic
from . import forms


class SignUp(generic.CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'twitter/signup.html'


@login_required
def index(request):
    latest_twit_list = Twit.objects.order_by('-pub_date')
    template = loader.get_template('twitter/index.html')
    context = {
        'latest_twit_list': latest_twit_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def send_twit(request):
    if request.method == 'POST':
        twit_form = forms.TwitForm(request.POST)
        if twit_form.is_valid():
            instance = twit_form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
    else:
        twit_form = forms.TwitForm()
    return render(request, 'twitter/user.html', {'twit_form': twit_form})

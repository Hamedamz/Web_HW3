from django.urls import reverse_lazy
from django.views import generic
from website import forms
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from user.models import Profile
from django.contrib.sessions.models import Session


class SignUp(generic.CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'user/signup.html'


@login_required
def loginn(request):
    try:
        prof = request.user.profile
    except:
        prof = Profile(pic='ahmad', user=request.user, ke=request.session.session_key)
        prof.save()
        return redirect('/')
    try:
        sess = prof.ke
    except:
        prof.ke = request.session.session_key
        return redirect('/')
    for s in Session.objects.all():
        if s.session_key == sess:
            s.delete()

    prof.ke = request.session.session_key
    prof.save()
    return redirect('/')

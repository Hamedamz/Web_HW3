from django.urls import reverse_lazy
from django.views import generic
from website import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from user.models import Profile
from django.contrib.sessions.models import Session
from django.contrib.auth import login as dj_login
from ids.models import Report
from website.forms import SignInForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import HttpResponse


class SignUp(generic.CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'user/signup.html'


def login(request):
    flag = False
    if request.user.is_authenticated:
        return redirect('/accounts')

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if Report.objects.filter(remote_address=request.META.get('REMOTE_ADDR')).order_by('-date_time')[0].nn > 15:
            flag = True
            try:
                send_mail(
                    'Subject here',
                    'Here is the message.',
                    'from@example.com',
                    [User.objects.get(username=form.username).email],
                    fail_silently=False,
                )
            except:
                pass
        if form.is_valid():
            cd = form.cleaned_data
            user = form.user
            dj_login(request, user)
            return redirect('/accounts')
    else:
        form = SignInForm()

    return render(request, 'registration/login.html', {
        'form': form,
        'captcha': flag
    })


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
            if s.session_key != request.session.session_key:
                s.delete()

    prof.ke = request.session.session_key
    prof.save()
    return redirect('/')

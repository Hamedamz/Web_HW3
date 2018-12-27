from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Twit
from website import forms
from user.models import Profile


@login_required
def index(request):
    latest_twit_list = Twit.objects.order_by('-pub_date')
    template = loader.get_template('twitter/index.html')
    pic=Profile.objects.all()[0].pic.url
    context = {
        'pic':pic,
        'latest_twit_list': latest_twit_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def send_twit(request):
    if request.method == 'POST':
        twit_form = forms.TwitForm(request.POST)
        pic_form = forms.PicForm(request.POST)
        if twit_form.is_valid():
            instance = twit_form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
        if pic_form.is_valid():
            instance = pic_form.save(commit=False)
            if Profile.objects.get(user=request.user) is None:
                instance.user=request.user
                instance.save()
            else:
                request.user.profile.pic=instance.pic
            return redirect('/')

    twit_form = forms.TwitForm()
    pic_form=forms.PicForm()

    return render(request, 'twitter/user.html', {'twit_form': twit_form, 'pic_form': pic_form})

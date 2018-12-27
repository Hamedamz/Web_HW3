from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from api.models import Sess
from twitter.models import Twit

@csrf_exempt
def index(request):
    pas=request.POST.get('password')
    user=request.POST.get('username')
    userFound=authenticate(username=user,password=pas)
    if userFound is not None:
        temp=Sess(user=userFound)
        temp.save()
        return HttpResponse(temp.id)
    else:
        return HttpResponse('GFYS')


@csrf_exempt
def twiting(request):
    key=request.POST.get('key')
    try:
        ses=Sess.objects.get(id__exact=key)
        title=request.POST.get('title')
        text=request.POST.get('text')
        twit=Twit(user=ses.user,title=title,text=text)
        twit.save()
        return HttpResponse('added')
    except:
        return HttpResponse('GFYS')

from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from api.models import Sess
from twitter.models import Twit
from ids.models import Report


@csrf_exempt
def indexv1(request):
    if Report.objects.filter(remote_address=request.META.get('REMOTE_ADDR')).order_by('-date_time')[0].nn>15:
        return HttpResponse('Request Blocked')
    pas = request.POST.get('password')
    user = request.POST.get('username')
    userFound = authenticate(username=user, password=pas)
    if userFound is not None:
        try:
            sess = Sess.objects.get(user__exact=userFound)
            return HttpResponse(sess.uid)


        except:
            temp = Sess(user=userFound)
            temp.save()
            return HttpResponse(temp.uid)
    else:
        return HttpResponse('GFYS')


@csrf_exempt
def twitingv1(request):
    if Report.objects.filter(remote_address=request.META.get('REMOTE_ADDR')).order_by('-date_time')[0].nn>15:
        return HttpResponse('Request Blocked')
    key = request.POST.get('key')
    try:
        ses = Sess.objects.get(uid__exact=key)
        title = request.POST.get('title')
        text = request.POST.get('text')
        twit = Twit(user=ses.user, title=title, text=text)
        twit.save()
        # request.user.
        return HttpResponse('added')
    except:
        return HttpResponse('GFYS')


def twitingv2(request):
    return HttpResponse(request.session['ahmad'])

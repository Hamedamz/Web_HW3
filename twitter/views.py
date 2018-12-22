from django.http import HttpResponse
from django.template import loader

from .models import Twit


def index(request):
    latest_twit_list = Twit.objects.order_by('-pub_date')
    template = loader.get_template('twitter/index.html')
    context = {
        'latest_twit_list': latest_twit_list,
    }
    return HttpResponse(template.render(context, request))

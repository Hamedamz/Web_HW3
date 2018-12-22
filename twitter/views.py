from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Twit
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
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

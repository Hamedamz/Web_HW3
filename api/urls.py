from django.urls import path,include

from . import views

urlpatterns = [
    path('v1/login', views.index),
    path('v1/tweet', views.twiting),
    # path('v2/tweet',include('django.contrib.auth.urls')),
]
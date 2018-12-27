from django.urls import path,include

from . import views

urlpatterns = [
    path('v1/login', views.indexv1),
    path('v1/tweet', views.twitingv1),
    path('v2/tweet', views.twitingv2),
]
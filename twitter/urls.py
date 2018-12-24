from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/', views.send_twit, name='twit'),
    path('accounts/', include('django.contrib.auth.urls')),
]
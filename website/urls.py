"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('twitter.urls')),
    url( 'login2/',auth_views.LoginView.as_view(template_name="registration/login1.html")),
    path('login/',views.login),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('logoutLastSessions/', views.loginn),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

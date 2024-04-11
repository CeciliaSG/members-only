"""
URL configuration for city_guide project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core.views import register



urlpatterns = [

    #Django admin
     path('admin/', admin.site.urls),

    # Allauth url
    path("accounts/", include("allauth.urls")),  
   

    # Custom Urls
    path('', include('content_management.urls')),
    path('core/', register, name='registration'),
    path('summernote/', include('django_summernote.urls')),
    path('event_management/', include('event_management.urls')), 
    path('core/', include('core.urls')),
     path('rsvp/', include('rsvp.urls')),
]
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
from core.views import register, edit_user_profile, UpdateUserProfileView
#from content_management.views import home
#from .views import edit_user_profile


urlpatterns = [
  
    #path('accounts/', include('django.contrib.auth.urls')), 

    #Django admin
     path('admin/', admin.site.urls),

    # Allauth url
    path("accounts/", include("allauth.urls")),  
   

    # Custom Urls
    path('core/', register, name='registration'),
    path('summernote/', include('django_summernote.urls')),
    path('account/', edit_user_profile, name='profile'),
    path('', include('content_management.urls'), name='content_management'), 
    path('update-profile/', UpdateUserProfileView.as_view(), name='update_profile'),
]
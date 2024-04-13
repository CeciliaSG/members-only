from django.urls import path
from .views import event_list, event_detail
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('events/', event_list, name='event_list'),
path('events/<int:event_id>/', views.event_detail, name='event_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from .models import RSVP

class RSVPAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'response', 'num_guests')

# Register your models here.
admin.site.register(RSVP, RSVPAdmin)
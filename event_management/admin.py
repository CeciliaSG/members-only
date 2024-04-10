from django.contrib import admin
from .models import Event, Heading
from content_management.models import Post

class HeadingAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

def create_posts_for_events(modeladmin, request, queryset):
    for event in queryset:

         Post.objects.create(
            title=event.title,
            heading=event.heading,
            content=event.description,
            event=event,
            slug=event.slug,
            excerpt=event.excerpt,
            tag=event.tag,
            status=event.status,
            start_date=event.start_date,
            end_date=event.end_date
        )

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'heading', 'description', 'slug', 'excerpt', 'tag', 'status', 'start_date', 'end_date']

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'heading', 'description', 'slug', 'excerpt', 'tag', 'status', 'start_date', 'end_date']


# Register your models here.
admin.site.register(Heading, HeadingAdmin)
admin.site.register(Event, EventAdmin)



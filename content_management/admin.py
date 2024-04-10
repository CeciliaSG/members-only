from django.contrib import admin
from .models import Heading, Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_at')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'excerpt',)

class HeadingAdmin(SummernoteModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ['name']
    summernote_fields = ('name',)


# Register your models here.
admin.site.register(Heading, HeadingAdmin)

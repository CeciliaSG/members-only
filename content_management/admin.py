from django.contrib import admin
from .models import Heading, Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'tag', 'id',
                    'created_at', 'heading', 'neighbourhood')
    search_fields = ['title', 'author_username']
    list_filter = ('status', 'author')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


class HeadingAdmin(SummernoteModelAdmin):
    list_display = ('name', 'parent_heading', 'created_at')
    search_fields = ['name']


# Register your models here.
admin.site.register(Heading, HeadingAdmin)
admin.site.register(Comment)


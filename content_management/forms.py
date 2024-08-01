from django import forms

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """ Lets users comment on posts. From Blog walkthroug"""
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'heading', 'content', 'excerpt',
                  'status', 'tag', 'neighbourhood',
                  'featured_image', 'author', ]
        widgets = {
            'content': SummernoteWidget(),
        }

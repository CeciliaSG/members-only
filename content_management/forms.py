from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """ Lets users comment on posts. From Blog walkthroug"""
    class Meta:
        model = Comment
        fields = ('body',)

from django.views import generic
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post


# Create your views here.
class PostListView(generic.ListView):
    template_name = "content_management/index.html"
    posts = Post.objects.filter(status=1)
    context_object_name = 'posts'
    model = Post    


def post_detail(request, slug):

    """
    Filter for status and slug and display on post_detail template
    """
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(Post, slug=slug)

    return render(
        request,
        "content_management/post_detail.html",
        {"post": post},
    )


def tag_filter(request, tag):

    """
    Filter for tag and display on template
    """
    posts = Post.objects.filter(tag=tag, status=1)
    context = {
        'tag': tag,
        'posts': posts
    }

    return render(request, 'content_management/restaurants_bars.html', context)


def post_tag_detail(request, tag):

    """
    Filter for status and tag and display on post_detail template
    """
    posts = Post.objects.filter(tag=tag, status=1)

    post = posts.first()

    return render(
        request,
        "content_management/post_detail.html",
        {"post": post, "tag": tag},
    )


 

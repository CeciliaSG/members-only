from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post, SavedPost, LikedPost
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
class PostListView(generic.ListView):
    template_name = "content_management/index.html"
    posts = Post.objects.filter(status=1)
    context_object_name = 'posts'
    model = Post    

    def get_queryset(self):
        return Post.objects.filter(status=1)


def post_list_view(request, Post):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(Post, tag=tag)

    return render(
        request,
        "content_management/post_detail.html",
        {"post": post},
    )


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
    Filter for status and tag and display on post_detail template.
    """
    posts = Post.objects.filter(tag=tag, status=1)
    post = posts.first()

    return render(
        request,
        "content_management/post_detail.html",
        {"post": post, "tag": tag},
    )

@login_required
def save_post(request, post_id):

    """
    Save the post to the database.
    """
    post = Post.objects.get(id=post_id)
    saved_post = SavedPost(user=request.user, post=post)
    saved_post.save()

    return HttpResponse("Post saved successfully!")

@login_required
def like_post(request, post_id):

    """
    like the post and save to the database.
    """
    post = Post.objects.get(id=post_id)
    liked_post = SavedPost(user=request.user, post=post)
    liked_post.save()

    return HttpResponse("Liked saved successfully!")    
 

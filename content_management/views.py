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
    Checks if the post is already saved, if not save the post to the database.
    """

    if request.user.saved_posts.filter(id=post_id).exists():
         return HttpResponse("The post has already been saved!")    

    post = Post.objects.get(id=post_id)
    saved_post = SavedPost(user=request.user, post=post)
    saved_post.save()

    return HttpResponse("Post saved successfully!")

@login_required
def like_post(request, post_id):

    """
    Check if the post has already been liked, if not save like to the database.
    """
    if request.user.liked_posts.filter(id=post_id).exists():
        return HttpResponse("The post has already been liked!")   

    post = Post.objects.get(id=post_id)
    liked_post = LikedPost(user=request.user, post=post)
    liked_post.save()

    return HttpResponse("You liked the post!")    

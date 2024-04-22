from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post, SavedPost, LikedPost, Heading
from django.contrib import messages
from django.http import HttpResponse


# Create your views here
class PostListView(generic.ListView):
    template_name = "content_management/index.html"
    posts = Post.objects.filter(status=1)
    context_object_name = 'posts'
    model = Post    

    def get_queryset(self):
        return Post.objects.filter(status=1)


def post_detail(request, slug):

    """
    Filter for status and slug,
    and display on post_detail template.
    """
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(Post, slug=slug)

    return render(
        request,
        "content_management/post_detail.html",
        {"post": post},
    )

class PostListByHeadingView(generic.ListView):
    template_name = "content_management/index.html"
    context_object_name = 'posts'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        heading_id = self.kwargs.get('heading_id')
        parent_heading_name = self.kwargs.get('parent_heading_name')

        context['heading'] = Heading.objects.filter(id=heading_id)
        context['parent_heading'] = Heading.objects.filter(name=parent_heading_name)
        
        return context

    def get_queryset(self):
        heading_id = self.kwargs.get('heading_id')
        return Post.objects.filter(heading__id=heading_id, status=1)


def tag_filter(request, template_name, tag):

    """
    Filter for tag and display on templates.
    """
    posts = Post.objects.filter(tag=tag, status=1)
    context = {
        'tag': tag,
        'posts': posts
    }

    return render(request, template_name, context)

def restaurants_bars_view(request, tag):
    template_name = 'content_management/restaurants_bars.html'
    return tag_filter(request, template_name, tag)

def things_to_do_view(request, tag):
    template_name = 'content_management/things_to_do.html'
    return tag_filter(request, template_name, tag)    

def neighbourhoods_list_view(request):
    posts_with_neighbourhoods = Post.objects.exclude(neighbourhood__isnull=True).exclude(neighbourhood__isnull=True).exclude(neighbourhood='')
        
    context = {
        'posts': posts_with_neighbourhoods
    }

    template_name = 'content_management/neighbourhoods.html'
    return render(request, template_name, context)
    


def post_tag_detail(request, tag):

    """
    Filter for status and tag, and display on post_detail template.
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
    Checks if the post is already saved, 
    un-save if saved, if not saved save to the database.
    """

    post = get_object_or_404(Post, id=post_id)

    try:
        saved_post = SavedPost.objects.get(user=request.user, post_id=post_id)
        saved_post.delete()
        return JsonResponse({'message': "You already saved this post. It is now unsaved!"})

    except SavedPost.DoesNotExist:
  
        post = Post.objects.get(id=post_id)
        saved_post = SavedPost(user=request.user, post=post)
        saved_post.save()    

    return JsonResponse({'message': "Post saved successfully!"})
    

@login_required
def like_post(request, post_id):

    """
    Check if the post has already been liked, 
    delete like if already liked, 
    if not save like to the database.
    """

    post = get_object_or_404(Post, id=post_id)

    try:
        liked_post = LikedPost.objects.get(user=request.user, post_id=post_id)
        liked_post.delete()
        return JsonResponse({'message': "You unliked the post!"})

    except LikedPost.DoesNotExist:
  
        post = Post.objects.get(id=post_id)
        #liked_post = LikedPost(user=request.user, post=post)
        liked_post = LikedPost(user=request.user, post=post, button_color='red')

        liked_post.save()

    
        return JsonResponse({'message': "You liked the post!"})

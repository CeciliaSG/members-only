from django.views import generic
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post


# Create your views here.
class PostListView(generic.ListView):
    template_name = "content_management/index.html"
    queryset = Post.objects.filter(status=1)
    context_object_name = 'posts'
    model = Post    

#def home(request):
    #return PostList.as_view()(request)

def post_detail(request, slug):

    """
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "content_management/post_detail.html",
        {"post": post},
    )

def like_post(request):
    if request.method == 'POST' and request.is_ajax():
        user_id = request.POST.get('user_id')
        post_id = request.POST.get('post_id')

        post = get_object_or_404(Post, id=post_id)

        is_liked = False
        if post.likes.filter(id=user_id).exists():
            post.likes.remove(request.user)
            is_liked = False
        else:
            post.likes.add(request.user)
            is_liked = True

        response_data = {
            'is_liked': is_liked,
            'likes_count': post.likes.count()
        }
        return JsonResponse(response_data)  
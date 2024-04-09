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

 

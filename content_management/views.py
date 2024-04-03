from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from .models import Heading, Post


# Create your views here.
class PostList(generic.ListView):
    template_name = "content_management/index.html"
    queryset = Post.objects.filter(status=1)
    context_object_name = 'posts'
    model = Post    

def home(request):
    return PostList.as_view()(request)
   

from django.shortcuts import render
from django.views import generic
from .models import Heading, Post


# Create your views here.
class PostList(generic.ListView):
    template_name = "content_management/post_list.html"
    queryset = Post.objects.filter(status=1)
    context_object_name = 'posts'
    model = Post    

def home(request):

    #return HttpResponse("Hello, City Guide1")
    return render(request, 'content_management/post_list.html')
   

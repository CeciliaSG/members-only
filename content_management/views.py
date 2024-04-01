from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(request, 'content_management/index.html')

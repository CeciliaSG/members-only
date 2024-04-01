from django.shortcuts import render
from django.http import HttpResponse
from .models import Heading


# Create your views here.
def index(request):

    return render(request, 'content_management/index.html')
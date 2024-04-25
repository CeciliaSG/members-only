from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Heading(models.Model):
    name = models.CharField(max_length=100)
    parent_heading = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
     
STATUS = ((0, "Draft"), (1, "Published"))     

class Event(models.Model):
    title = models.CharField(max_length=500)
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(blank=True)
    tag = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS, default=0) 
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title



from django.db import models
from django.contrib.auth.models import User
from event_management.models import Event
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

class Post(models.Model):
    title = models.CharField(max_length=255)
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    tag = models.CharField(max_length=50, null=True)
    featured_image = CloudinaryField('image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    status = models.IntegerField(choices=STATUS, default=0)     

class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title

    class Meta:
        unique_together = ('user', 'post')

class LikedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

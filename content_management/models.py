from django.db import models

# Create your models here.
from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        
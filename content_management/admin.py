from django.contrib import admin
from .models import Heading
from .models import Post

# Register your models here.
admin.site.register(Heading)
admin.site.register(Post)

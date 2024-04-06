from django.db import models
from content_management.models import Post
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class UserProfile(models.Model):

    CITY_CHOICES = [
        ('stockholm', 'Stockholm'),
     ]

    NEIGHBOURHOOD_CHOICES = [
        ('östermalm', 'Östermalm'),
        ('norra djurgårdsstaden', 'Norra Djurgårdsstaden'),
        ('vasastan', 'Vasastan'),
        ('norrmalm', 'Norrmalm'),
        ('gamlastan', 'Gamlastan'),
        ('södermalm', 'Södermalm'),
    ]

    INTEREST_CHOICES = [
        ('restaurants', 'Restaurants'),
        ('bars', 'Bars'),
        ('events', 'Events'),
         ('whats on', 'Whats On'),
     ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    neighbourhood = models.CharField(max_length=100, choices=NEIGHBOURHOOD_CHOICES)
    interests = ArrayField(models.CharField(max_length=100, choices=INTEREST_CHOICES), blank=True)


def __str__(self):
        return self.user.username

def edit_user_profile(request):
    if request.method == 'POST':
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=request.user.userprofile)
            if form.is_valid():
                form.save()
                return redirect('profile')
    else:
            form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {'form': form}) 

class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"
          



from django.db import models
from content_management.models import Post
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class UserProfile(models.Model):

    """
    Saves a single user profile for a user related to :model:`User`.
    """

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
    neighbourhood = models.CharField(max_length=100,
                                     choices=NEIGHBOURHOOD_CHOICES)
    interests = ArrayField(models.CharField(max_length=100,
                                            choices=INTEREST_CHOICES),
                           blank=True)


def __str__(self):

    return self.user.username


def edit_user_profile(request):
    """
    Updates a single user profile for a user related to :models:`UserProfile`.
    """

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {'form': form})

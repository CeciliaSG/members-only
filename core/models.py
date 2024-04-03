from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    CITY_CHOICES = [
        ('stockholm', 'Stockholm'),
     ]

    NEIGHBOURHOOD_CHOICES = [
        ('östermalm', 'Östermalm'),
        ('norra djurgårdsstaden', 'norra djurgårdsstaden'),
        ('vasastan', 'Vasastan'),
        ('norrmalm', 'Norrmalm'),
        ('gamlastan', 'Gamlastan'),
        ('södermalm', 'Södermalm'),
    ]

    INTEREST_CHOICES = [
        ('restaurants', 'restaurants'),
        ('bars', 'Bars'),
        ('events', 'Events'),
         ('whats on', 'Whats On'),
         
     ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    neighbourhood = models.CharField(max_length=100, choices=NEIGHBOURHOOD_CHOICES)
    interests = models.CharField(max_length=100, choices=INTEREST_CHOICES)

def __str__(self):
        return self.user.username



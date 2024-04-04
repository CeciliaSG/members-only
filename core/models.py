from django.db import models
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
    email = models.EmailField(max_length=255, unique=True)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    neighbourhood = models.CharField(max_length=100, choices=NEIGHBOURHOOD_CHOICES)
    #interests = models.CharField(max_length=100, choices=INTEREST_CHOICES)
    interests = ArrayField(models.CharField(max_length=100, choices=INTEREST_CHOICES), blank=True)

def __str__(self):
        return self.user.username



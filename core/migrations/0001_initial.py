# Generated by Django 4.2.11 on 2024-04-03 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('stockholm', 'Stockholm')], max_length=100)),
                ('neighbourhood', models.CharField(choices=[('östermalm', 'Östermalm'), ('norra djurgårdsstaden', 'norra djurgårdsstaden'), ('vasastan', 'Vasastan'), ('norrmalm', 'Norrmalm'), ('gamlastan', 'Gamlastan'), ('södermalm', 'Södermalm')], max_length=100)),
                ('interests', models.CharField(choices=[('restaurants', 'restaurants'), ('bars', 'Bars'), ('events', 'Events'), ('whats on', 'Whats On')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

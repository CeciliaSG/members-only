# Generated by Django 4.2.11 on 2024-04-17 08:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content_management', '0013_post_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AlterUniqueTogether(
            name='savedpost',
            unique_together={('user', 'post')},
        ),
    ]

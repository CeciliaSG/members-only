# Generated by Django 4.2.11 on 2024-04-14 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content_management', '0010_savedpost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='LikedPost',
        ),
        migrations.AlterField(
            model_name='savedpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
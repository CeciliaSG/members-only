# Generated by Django 4.2.11 on 2024-04-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]

# Generated by Django 4.2.11 on 2024-04-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0005_remove_event_image_event_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
# Generated by Django 4.2.11 on 2024-04-22 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0017_likedpost_button_color_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='likedpost',
            unique_together=set(),
        ),
    ]

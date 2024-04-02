# Generated by Django 4.2.11 on 2024-04-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]

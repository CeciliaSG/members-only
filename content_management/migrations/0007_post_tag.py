# Generated by Django 4.2.11 on 2024-04-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0006_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
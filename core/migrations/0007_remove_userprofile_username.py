# Generated by Django 4.2.11 on 2024-04-05 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_userprofile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]

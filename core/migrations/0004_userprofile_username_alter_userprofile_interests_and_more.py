# Generated by Django 4.2.11 on 2024-04-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='default_username', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.CharField(choices=[('restaurants', 'Restaurants'), ('bars', 'Bars'), ('events', 'Events'), ('whats on', 'Whats On')], max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='neighbourhood',
            field=models.CharField(choices=[('östermalm', 'Östermalm'), ('norra djurgårdsstaden', 'Norra Djurgårdsstaden'), ('vasastan', 'Vasastan'), ('norrmalm', 'Norrmalm'), ('gamlastan', 'Gamlastan'), ('södermalm', 'Södermalm')], max_length=100),
        ),
    ]
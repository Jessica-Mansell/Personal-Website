# Generated by Django 4.0.5 on 2022-08-23 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0010_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]

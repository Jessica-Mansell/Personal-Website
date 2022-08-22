# Generated by Django 4.0.5 on 2022-08-22 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0008_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]

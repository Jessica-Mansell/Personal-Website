# Generated by Django 4.0.5 on 2022-08-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Jessica&#39s Tech Blog', max_length=255),
        ),
    ]

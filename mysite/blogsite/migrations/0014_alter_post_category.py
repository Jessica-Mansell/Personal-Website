# Generated by Django 4.0.5 on 2022-09-01 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0013_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(max_length=60, on_delete=django.db.models.deletion.CASCADE, related_name='catego', to='blogsite.category'),
        ),
    ]
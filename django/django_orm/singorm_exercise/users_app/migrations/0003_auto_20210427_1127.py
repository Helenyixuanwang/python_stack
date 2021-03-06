# Generated by Django 2.2 on 2021-04-27 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20210427_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 2.2 on 2021-06-13 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_app', '0006_auto_20210612_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='hobby_img',
            field=models.ImageField(default='default.jpeg', upload_to='images/'),
        ),
    ]

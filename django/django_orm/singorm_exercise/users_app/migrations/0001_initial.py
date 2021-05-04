# Generated by Django 2.2 on 2021-04-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('release_date', models.DateTimeField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]

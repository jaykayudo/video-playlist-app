# Generated by Django 3.1.3 on 2020-11-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_playlist_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='logo',
            field=models.FileField(upload_to=''),
        ),
    ]

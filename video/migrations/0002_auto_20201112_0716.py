# Generated by Django 3.1.3 on 2020-11-12 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='name',
            new_name='main_character',
        ),
        migrations.AddField(
            model_name='moviename',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='moviename',
            name='movie',
            field=models.CharField(default='Will Smith', max_length=1000),
            preserve_default=False,
        ),
    ]

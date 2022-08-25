# Generated by Django 4.1 on 2022-08-25 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0010_genre_album_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='albums.genre'),
        ),
    ]
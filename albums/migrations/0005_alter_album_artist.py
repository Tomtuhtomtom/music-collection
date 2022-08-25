# Generated by Django 4.1 on 2022-08-25 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_alter_album_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='albums.artist'),
        ),
    ]
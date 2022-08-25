# Generated by Django 4.1 on 2022-08-25 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0009_alter_album_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a music genre', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this album', to='albums.genre'),
        ),
    ]
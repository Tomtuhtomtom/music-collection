# Generated by Django 4.1 on 2022-08-25 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0013_album_image_image_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Cover',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='image',
            new_name='cover',
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-19 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0005_place_img_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='type',
            new_name='location',
        ),
    ]

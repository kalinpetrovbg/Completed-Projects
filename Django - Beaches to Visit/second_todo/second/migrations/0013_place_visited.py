# Generated by Django 3.2.4 on 2021-06-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0012_place_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='visited',
            field=models.BooleanField(default=False),
        ),
    ]

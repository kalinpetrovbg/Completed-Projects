# Generated by Django 3.2.4 on 2021-06-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0011_remove_place_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

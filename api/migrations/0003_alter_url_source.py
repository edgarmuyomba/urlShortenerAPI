# Generated by Django 4.2.4 on 2023-08-21 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_url_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='source',
            field=models.URLField(unique=True),
        ),
    ]
# Generated by Django 3.2.9 on 2023-02-01 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0009_alter_urlshortener_original_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='original_url',
            field=models.URLField(max_length=250),
        ),
    ]

# Generated by Django 3.2.9 on 2023-01-31 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='shortened_url_code',
            field=models.CharField(max_length=20),
        ),
    ]

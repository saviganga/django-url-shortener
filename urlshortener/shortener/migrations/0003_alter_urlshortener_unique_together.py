# Generated by Django 3.2.9 on 2023-01-31 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_alter_urlshortener_shortened_url_code'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='urlshortener',
            unique_together=set(),
        ),
    ]
# Generated by Django 3.2.9 on 2023-01-31 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_alter_urlshortener_shortened_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='original_url',
            field=models.CharField(max_length=250),
        ),
    ]
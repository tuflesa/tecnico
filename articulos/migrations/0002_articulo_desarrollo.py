# Generated by Django 3.1.7 on 2025-01-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='desarrollo',
            field=models.IntegerField(default=507),
        ),
    ]

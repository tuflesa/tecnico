# Generated by Django 3.1.7 on 2021-10-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0028_stockminimo_localizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockminimo',
            name='stock_pendiente',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.1.7 on 2021-11-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0035_remove_stockminimo_stock_act'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockminimo',
            name='stock_act',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

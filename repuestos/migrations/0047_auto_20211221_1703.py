# Generated by Django 3.1.7 on 2021-12-21 16:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0046_auto_20211221_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

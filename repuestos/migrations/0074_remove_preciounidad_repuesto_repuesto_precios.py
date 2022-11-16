# Generated by Django 4.0.4 on 2022-11-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0073_preciounidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preciounidad',
            name='repuesto',
        ),
        migrations.AddField(
            model_name='repuesto',
            name='precios',
            field=models.ManyToManyField(related_name='precios', to='repuestos.preciounidad'),
        ),
    ]

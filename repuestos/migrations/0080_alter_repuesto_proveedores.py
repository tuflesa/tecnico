# Generated by Django 4.0.4 on 2022-11-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0079_rename_preciounidad_preciorepuesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesto',
            name='proveedores',
            field=models.ManyToManyField(blank=True, related_name='repuestos', to='repuestos.proveedor'),
        ),
    ]

# Generated by Django 3.1.7 on 2025-02-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0013_auto_20241203_0710'),
        ('repuestos', '0114_auto_20250217_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesto',
            name='equipos',
            field=models.ManyToManyField(blank=True, null=True, related_name='repuestos', to='estructura.Equipo'),
        ),
    ]

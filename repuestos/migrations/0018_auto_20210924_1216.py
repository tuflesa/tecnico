# Generated by Django 3.1.7 on 2021-09-24 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0017_repuesto_tipo_repuesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesto',
            name='tipo_repuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repuestos.tiporepuesto'),
        ),
    ]

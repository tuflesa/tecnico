# Generated by Django 4.0.4 on 2022-11-02 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0072_alter_lineapedido_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecioUnidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('proveedor', models.ManyToManyField(to='repuestos.proveedor')),
                ('repuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repuestos.repuesto')),
            ],
        ),
    ]

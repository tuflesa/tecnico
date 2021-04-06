# Generated by Django 3.1.7 on 2021-04-06 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0006_auto_20210405_2213'),
        ('repuestos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuesto',
            name='equipo',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repuestos', to='estructura.equipo'),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='fabricante',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='modelo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='stock_minimo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='repuesto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 4.0.4 on 2022-11-17 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0081_alter_lineapedido_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineapedido',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lineapedido',
            name='por_recibir',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

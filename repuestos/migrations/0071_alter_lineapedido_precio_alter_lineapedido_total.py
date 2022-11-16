# Generated by Django 4.0.4 on 2022-10-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0070_alter_lineapedido_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineapedido',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='lineapedido',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0005_auto_20210405_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='fabricante',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='modelo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='numero',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

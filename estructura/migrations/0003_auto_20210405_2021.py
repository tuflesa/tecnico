# Generated by Django 3.1.7 on 2021-04-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0002_equipo_seccion_zona'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='siglas',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='zona',
            name='siglas',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

# Generated by Django 3.1.7 on 2021-09-24 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0015_repuesto_descatalogado'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoRepuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
    ]

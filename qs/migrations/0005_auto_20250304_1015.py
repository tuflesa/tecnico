# Generated by Django 3.1.7 on 2025-03-04 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qs', '0004_auto_20241228_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variante',
            old_name='l_saluda_sup',
            new_name='l_salida_sup',
        ),
    ]

# Generated by Django 3.1.7 on 2023-08-04 07:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rodillos', '0018_merge_20230630_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='revision',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

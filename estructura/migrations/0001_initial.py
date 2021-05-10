# Generated by Django 3.1.7 on 2021-05-04 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('siglas', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('siglas', models.CharField(max_length=10, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zonas', to='estructura.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secciones', to='estructura.zona')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fabricante', models.CharField(blank=True, max_length=50, null=True)),
                ('modelo', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(blank=True, max_length=50, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='equipos')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='estructura.seccion')),
            ],
        ),
    ]

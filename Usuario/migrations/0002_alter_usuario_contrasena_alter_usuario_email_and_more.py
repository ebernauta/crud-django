# Generated by Django 4.1.2 on 2022-11-04 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(max_length=50, verbose_name='contrasena'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=50, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ingreso',
            field=models.CharField(max_length=50, verbose_name='ingreso'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='rut'),
        ),
    ]

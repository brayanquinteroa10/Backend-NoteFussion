# Generated by Django 4.2a1 on 2023-02-12 00:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fechaDesde',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fechaHasta',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
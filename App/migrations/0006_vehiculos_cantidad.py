# Generated by Django 5.1.1 on 2024-10-04 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_vehiculos_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculos',
            name='Cantidad',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
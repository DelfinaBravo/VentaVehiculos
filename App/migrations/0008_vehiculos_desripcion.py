# Generated by Django 5.1.1 on 2024-10-04 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_vehiculos_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculos',
            name='Desripcion',
            field=models.TextField(max_length=50, null=True),
        ),
    ]

# Generated by Django 5.2.4 on 2025-07-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitante',
            name='cedula_pasaporte',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

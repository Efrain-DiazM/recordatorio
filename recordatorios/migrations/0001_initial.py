# Generated by Django 5.0.6 on 2024-05-25 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recordatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_medicamento', models.CharField(max_length=200)),
                ('hora_alerta', models.TimeField()),
                ('comentario', models.TextField()),
            ],
        ),
    ]

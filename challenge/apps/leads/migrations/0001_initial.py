# Generated by Django 3.2.2 on 2022-05-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(help_text='Correo Electrónico', max_length=254, unique=True)),
                ('file_number', models.CharField(help_text='Número de Legajo/Expediente', max_length=20, unique=True)),
                ('address', models.CharField(default='', max_length=255)),
                ('phone_number', models.CharField(default='', max_length=64)),
            ],
            options={
                'db_table': 'Students',
            },
        ),
    ]

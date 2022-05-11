# Generated by Django 3.2.2 on 2022-05-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=128, verbose_name='name')),
                ('course_duration', models.PositiveSmallIntegerField(verbose_name='duration')),
                ('passed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'courses',
            },
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
    ]

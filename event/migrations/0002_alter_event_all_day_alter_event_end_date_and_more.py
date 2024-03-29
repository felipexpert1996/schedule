# Generated by Django 4.0.5 on 2022-09-18 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='all_day',
            field=models.BooleanField(help_text='O evento vai durar o dia inteiro?'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(help_text='Data final do evento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(help_text='Hora final do evento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(help_text='Data inicial do evento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(help_text='Hora inicial do evento'),
        ),
    ]

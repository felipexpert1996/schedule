# Generated by Django 4.0.5 on 2022-10-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_all_day_alter_event_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='teste', help_text='Titulo do evento', max_length=100),
            preserve_default=False,
        ),
    ]
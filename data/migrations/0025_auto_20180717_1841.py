# Generated by Django 2.0.5 on 2018-07-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0024_auto_20180717_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='registration_end_date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Registration Ends On (IST) '),
        ),
        migrations.AddField(
            model_name='event',
            name='registration_start_date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Registration Starts On (IST) '),
        ),
    ]

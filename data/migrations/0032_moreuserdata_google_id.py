# Generated by Django 2.0.5 on 2018-08-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0031_auto_20180812_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='moreuserdata',
            name='google_id',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

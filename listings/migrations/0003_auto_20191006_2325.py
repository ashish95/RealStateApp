# Generated by Django 2.2.6 on 2019-10-06 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20191004_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 6, 23, 25, 22, 240277)),
        ),
    ]

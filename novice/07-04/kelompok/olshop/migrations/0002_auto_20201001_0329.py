# Generated by Django 3.1 on 2020-10-01 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjualan1m',
            name='tanggal',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
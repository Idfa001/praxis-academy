# Generated by Django 3.1 on 2020-09-16 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0005_auto_20200916_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjualan1m',
            name='kuantitas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='penjualan2m',
            name='kuantitas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 3.1 on 2020-09-22 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjualan1m',
            name='tanggal',
            field=models.DateField(verbose_name='%d-%m-%Y'),
        ),
    ]

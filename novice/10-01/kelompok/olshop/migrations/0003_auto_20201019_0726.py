# Generated by Django 3.1.2 on 2020-10-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0002_auto_20201019_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjualan1m',
            name='jatuh_tempo',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]

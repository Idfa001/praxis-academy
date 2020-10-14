# Generated by Django 3.1.2 on 2020-10-09 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0005_auto_20201008_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pem_tunaim',
            old_name='jumlah',
            new_name='kas_keluar',
        ),
        migrations.RemoveField(
            model_name='pem_tunaim',
            name='catatan',
        ),
        migrations.AddField(
            model_name='pem_tunaim',
            name='dibayar',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='pem_tunaim',
            name='pembelian',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
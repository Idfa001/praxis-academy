# Generated by Django 3.1 on 2020-09-15 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0005_pembayaran_biayam'),
    ]

    operations = [
        migrations.CreateModel(
            name='pembayaran_lainm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('keterangan', models.CharField(max_length=200)),
                ('utang', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dibayar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('catatan', models.TextField(default='')),
            ],
        ),
    ]

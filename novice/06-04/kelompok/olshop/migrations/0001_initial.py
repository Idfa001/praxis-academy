# Generated by Django 3.1 on 2020-09-24 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='barangm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barang', models.CharField(max_length=200)),
                ('harga_beli', models.IntegerField(default=0)),
                ('harga_jual', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='pem_kreditm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('keterangan', models.CharField(max_length=200)),
                ('jumlah', models.DecimalField(decimal_places=0, max_digits=10)),
                ('catatan', models.CharField(max_length=200)),
                ('dibayar1', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='pem_lainm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('keterangan', models.CharField(max_length=200)),
                ('dibayar', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('utang', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('catatan', models.CharField(max_length=200)),
                ('dibayar2', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='pem_tunaim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('keterangan', models.CharField(max_length=200)),
                ('jumlah', models.DecimalField(decimal_places=0, max_digits=10)),
                ('catatan', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='pembayaran_biayam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('keterangan', models.CharField(max_length=200)),
                ('dibayar', models.DecimalField(decimal_places=0, max_digits=10)),
                ('catatan', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='pembayaran_lainm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('keterangan', models.CharField(max_length=200)),
                ('dibayar', models.DecimalField(decimal_places=0, max_digits=10)),
                ('utang', models.DecimalField(decimal_places=0, max_digits=10)),
                ('catatan', models.CharField(max_length=200)),
                ('dibayar3', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='pend_lainm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('keterangan', models.CharField(max_length=200)),
                ('jumlah', models.DecimalField(decimal_places=0, max_digits=10)),
                ('piutang', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('catatan', models.CharField(max_length=200)),
                ('terima', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='penjualan3m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('keterangan', models.CharField(max_length=200)),
                ('kas', models.IntegerField(default=0)),
                ('piutang', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('catatan', models.CharField(max_length=200)),
                ('terima', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='utangm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('catatan', models.CharField(max_length=200)),
                ('jumlah', models.DecimalField(decimal_places=0, max_digits=10)),
                ('dibayar', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='penjualan2m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('kuantitas', models.IntegerField(default=0)),
                ('catatan', models.CharField(max_length=200)),
                ('terima', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='olshop.barangm')),
            ],
        ),
        migrations.CreateModel(
            name='penjualan1m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('kuantitas', models.IntegerField(default=0)),
                ('saldo_awal', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='olshop.barangm')),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-13 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0002_auto_20201013_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pem_kreditm',
            name='barang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='olshop.barangm'),
        ),
    ]

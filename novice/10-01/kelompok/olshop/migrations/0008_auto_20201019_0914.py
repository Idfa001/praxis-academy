# Generated by Django 3.1.2 on 2020-10-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0007_auto_20201019_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='pem_kreditm',
            name='jatuh_tempo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pem_lainm',
            name='jatuh_tempo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pem_tunaim',
            name='jatuh_tempo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pembayaran_lainm',
            name='jatuh_tempo',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-08 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olshop', '0003_utangm_jatuh_tempo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utangm',
            old_name='jatuh_tempo',
            new_name='tempo',
        ),
    ]

# Generated by Django 3.1 on 2020-08-27 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='artis',
        ),
    ]
# Generated by Django 3.1 on 2020-08-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_task_lirik'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='link',
            field=models.TextField(default=''),
        ),
    ]

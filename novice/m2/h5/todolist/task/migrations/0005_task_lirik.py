# Generated by Django 3.1 on 2020-08-28 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_task_th'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='lirik',
            field=models.TextField(default=''),
        ),
    ]
# Generated by Django 3.1.2 on 2020-10-15 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 16, 0, 10, 37, 191603), null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 16, 0, 10, 37, 191603), null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-19 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0032_auto_20201119_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterfeedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 10, 51, 34, 134490)),
        ),
    ]

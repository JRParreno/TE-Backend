# Generated by Django 3.1.2 on 2020-11-12 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0013_auto_20201111_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterfeedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 12, 13, 58, 41, 173024)),
        ),
    ]
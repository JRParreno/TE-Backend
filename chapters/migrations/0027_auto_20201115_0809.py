# Generated by Django 3.1.2 on 2020-11-15 08:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0026_auto_20201115_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterfeedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 8, 9, 5, 469449)),
        ),
    ]
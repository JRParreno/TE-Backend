# Generated by Django 3.1.2 on 2020-11-19 06:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0030_auto_20201119_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterfeedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 6, 46, 49, 889427)),
        ),
    ]

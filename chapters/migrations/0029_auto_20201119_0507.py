# Generated by Django 3.1.2 on 2020-11-19 05:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0028_auto_20201116_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterfeedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 5, 7, 24, 639956)),
        ),
    ]

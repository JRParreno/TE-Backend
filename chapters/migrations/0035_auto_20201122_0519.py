# Generated by Django 3.1.2 on 2020-11-22 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0034_auto_20201122_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterfeedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 5, 19, 14, 894759)),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-15 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0025_merge_20201112_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterfeedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 8, 3, 46, 987379)),
        ),
    ]

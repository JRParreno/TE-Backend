# Generated by Django 3.1.2 on 2020-11-10 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0009_auto_20201110_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterfeedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 9, 37, 2, 392285)),
        ),
    ]
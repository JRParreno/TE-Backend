# Generated by Django 3.1.2 on 2020-10-22 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0006_auto_20201022_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterfeedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 20, 59, 35, 671587)),
        ),
        migrations.AlterField(
            model_name='studentremarks',
            name='remarks',
            field=models.BooleanField(default=True),
        ),
    ]

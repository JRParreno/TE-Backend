# Generated by Django 3.1.2 on 2020-10-22 12:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chapters', '0003_auto_20201022_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentchapterfeedback',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentchapterfeedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 20, 13, 5, 693663)),
        ),
    ]
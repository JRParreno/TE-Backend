# Generated by Django 3.1.2 on 2020-11-19 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_auto_20201119_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.activitytype'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_activity_activity_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
# Generated by Django 3.1.2 on 2020-11-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0009_auto_20201115_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.IntegerField(null=True),
        ),
    ]
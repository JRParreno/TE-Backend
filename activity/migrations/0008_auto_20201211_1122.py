# Generated by Django 3.1.2 on 2020-12-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0007_activity_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['activity_number']},
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_number',
            field=models.IntegerField(null=True),
        ),
    ]
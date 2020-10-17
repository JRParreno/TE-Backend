# Generated by Django 3.1.2 on 2020-10-17 04:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('start', models.DateTimeField(default=datetime.datetime(2020, 10, 17, 12, 38, 55, 284972), null=True)),
                ('end', models.DateTimeField(default=datetime.datetime(2020, 10, 17, 12, 38, 55, 284972), null=True)),
                ('remarks', models.BooleanField(blank=True, null=True)),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sections.section')),
            ],
        ),
    ]

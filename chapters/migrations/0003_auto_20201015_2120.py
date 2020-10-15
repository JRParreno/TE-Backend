# Generated by Django 3.1.2 on 2020-10-15 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0002_studentchapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentchapter',
            name='chapter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chapters.chapter'),
        ),
        migrations.AlterField(
            model_name='studentchapter',
            name='feedback',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

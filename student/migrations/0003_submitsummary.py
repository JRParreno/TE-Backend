# Generated by Django 3.1.2 on 2020-11-19 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0011_auto_20201119_0646'),
        ('student', '0002_delete_submitanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=255, null=True)),
                ('table_image', models.ImageField(blank=True, null=True, upload_to='table_images')),
                ('code_file', models.FileField(blank=True, null=True, upload_to='code')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='question.question')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 3.1.2 on 2020-11-12 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_question_question_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerkey',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='question.question'),
        ),
    ]
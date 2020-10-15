from django.db import models
from activity.models import Activity
from django.contrib.auth.models import User


class Question(models.Model):

    QUESTION_TYPES = [
        ('IDENT', 'Identification'),
        ('MULT', 'Mutliple Choice')
    ]

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    q_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    number = models.IntegerField()

    def __str__(self):
        return self.q_type



class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False, null=True)
    description = models.CharField(max_length=100, null=True, blank=False)
    answer_key = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    choice = models.ForeignKey(Choices, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return self.choice

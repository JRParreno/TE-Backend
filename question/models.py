from django.db import models
from activity.models import Activity
from authentication.models import User


class Question(models.Model):

    class Meta:
        unique_together = [['activity', 'number']]

    QUESTION_TYPES = [
        ('IDENT', 'Identification'),
        ('MULT', 'Mutliple Choice')
    ]

    question_name = models.CharField(max_length=255, null=True, blank=False)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    q_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    number = models.IntegerField()
    answer = models.CharField(max_length=255, null=True, blank=False)
    points = models.IntegerField(null=True, blank=False)
    def __str__(self):
        return str(self.question_name)

    def choices(self):
        if not hasattr(self, '_choices'):
            self._choices = self.choices_set.all()
        return self._choices


class Choices(models.Model):

    class Meta:
        unique_together = [['question', 'description']]

    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False, null=True)
    description = models.CharField(max_length=100, null=True, blank=False)
    
    def __str__(self):
        return str(self.question)
    
    def activity_code(self):
        return str(self.question.activity)
    
    def get_chapter(self):
        return str(self.question.activity.chapter)





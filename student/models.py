from django.db import models
from authentication.models import User
from question.models import Question

class SubmitAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False, null=True)
    answer = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return str(self.user.username)
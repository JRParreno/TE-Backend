from django.db import models
from authentication.models import User
from question.models import Question


class SubmitSummary(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    answer = models.CharField(max_length=255, null=True, blank=True)
    table_image = models.ImageField(upload_to='table_images', null=True, blank=True)
    code_file = models.FileField(upload_to='code', null=True, blank=True)

    def __str__(self):
        return str(self.student)

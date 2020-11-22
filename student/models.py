from django.db import models
from authentication.models import User
from question.models import Question
from assesment.models import Assesment


class SubmitSummary(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=False)
    assesment = models.ForeignKey(Assesment, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    answer = models.CharField(max_length=255, null=True, blank=True)
    table_image = models.ImageField(upload_to='table_images', null=True, blank=True)
    code_file = models.FileField(upload_to='code', null=True, blank=True)

    def __str__(self):
        return str(self.student)


    @property
    def get_score(self):
        
        score = 0
        check_student = Assesment.objects.filter(activity=self.question.activity, student=self.student).values('score')
        
        if check_student.exists():
            get_student_score = check_student.first()
            score = get_student_score['score']
        return score
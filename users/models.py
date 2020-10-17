from django.db import models
from django.contrib.auth.models import User


# for student models
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    student_number = models.CharField(max_length=50, blank=True, null=False)

    def __str__(self):
        return self.student_number


# for professor
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    faculty_id = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.faculty_id

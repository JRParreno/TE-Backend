from django.db import models
from authentication.models import User
from sections.models import Section
from datetime import datetime


# for professor
class Chapter(models.Model):
    filename = models.CharField(max_length=100, null=False, blank=False)
    embbeded_url = models.CharField(max_length=255, null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.filename)


# student per chapter
class StudentRemarks(models.Model):
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, null=False, blank=False)  # get specific chapter
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    remarks = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)


class ChapterFeedback(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    student_chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, null=False, blank=False)  # get specific chapter student
    feedback = models.CharField(max_length=255, null=False, blank=False)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.user)

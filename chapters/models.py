from django.db import models
from django.contrib.auth.models import User
from sections.models import Section


# for professor
class Chapter(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    embbeded_url = models.CharField(max_length=255, null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


# student per chapter
class StudentChapter(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE) # get specific chapter
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    remarks = models.BooleanField(default=False, null=False, blank=False)
    feedback = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.chapter.title

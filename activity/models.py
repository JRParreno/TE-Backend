from django.db import models
from authentication.models import User
from sections.models import Section
from chapters.models import Chapter
from datetime import datetime
from django.shortcuts import get_object_or_404


# activity type
class ActivityType(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return str(self.name)


# activities
class Activity(models.Model):
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE, null=True, blank=False)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=False)
    activity_name = models.CharField(max_length=100, null=True, blank=False)
    total_score = models.IntegerField(null=True, blank=False)
    description = models.CharField(max_length=255, null=True, blank=False)
    activity_number = models.IntegerField(null=True, blank=False)

    class Meta:
        ordering = ['activity_number']

    def __str__(self):
        return str(self.activity_name)
    

class ProfActivity(models.Model):
    
    class Meta:
        unique_together = [['activity', 'section']]
    
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=False)
    start = models.DateField(null=True, blank=False)
    end = models.DateField(null=True, blank=False)
    remarks = models.BooleanField(default=False)
    # set start and end base in chapter and acitvity type
    def __str__(self):
        return str(self.section)

    @property
    def activity_description(self):
        profactivity = get_object_or_404(Activity, pk=self.activity.pk)
        return profactivity.description

class ActivityRemarks(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    remarks = models.BooleanField(default=True)

    def __str__(self):
        return str(self.remarks)
    
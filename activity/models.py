# from django.db import models
# from django.contrib.auth.models import User
# from sections.models import Section
# from datetime import datetime

# # activities
# class Activity(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=False)
#     section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=False)
#     start = models.DateTimeField(default=datetime.now(), null=True, blank=False)
#     end = models.DateTimeField(default=datetime.now(), null=True, blank=False)
#     remarks = models.BooleanField(null=True, blank=True)

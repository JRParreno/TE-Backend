# from django.db import models
# from django.contrib.auth.models import User


# # block models or section
# class Section(models.Model):
#     # instance from user (professor)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     code = models.CharField(max_length=50, null=False,
#                             blank=False)  # section code
#     schedule = models.CharField(
#         max_length=50, null=False, blank=False)  # schedule of section

#     def __str__(self):
#         return self.code

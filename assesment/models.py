# from django.db import models
# from django.contrib.auth.models import User
# from activity.models import Activity


# class Assesment(models.Model):
#     activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=False)
#     student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
#     score = models.FloatField(null=True, blank=False)
#     date_taken = models.DateField(auto_now=True)

#     def __str__(self):
#         return self.score

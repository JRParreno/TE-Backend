from django.db import models
from authentication.models import User
from activity.models import Activity
from django.db.models import Q, F

class Assesment(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    score = models.FloatField(null=True, blank=False)
    date_taken = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.score)

    @property
    def full_name(self):
        name = '{} {} {}'.format(self.student.last_name, self.student.first_name, self.student.middle_name)
        return name
    
    def submitsummary(self):
        if not hasattr(self, '_submitsummary'):
            self._submitsummary = self.submitsummary_set.filter(Q(question__q_type="CODE") | Q(question__q_type="TABLE"))
        return self._submitsummary
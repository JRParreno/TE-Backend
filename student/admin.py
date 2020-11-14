from django.contrib import admin
from .models import SubmitAnswer

@admin.register(SubmitAnswer)
class SectionStudentAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'user',
        'question',
        'answer',
    )
    list_filter = (
        'user',
        'question',
    )
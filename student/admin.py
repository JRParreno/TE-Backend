from django.contrib import admin
from .models import SubmitSummary


@admin.register(SubmitSummary)
class SubmitSummaryAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'student',
        'question',
        'answer',
        'table_image',
        'code_file',
    )
    list_filter = (
        'student',
        'question',
    )
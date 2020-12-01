from django.contrib import admin
from .models import SubmitSummary


@admin.register(SubmitSummary)
class SubmitSummaryAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'student',
        'assesment',
        'question',
        'answer',
        'table_image',
        'code_file',
        'remarks',
        'points'
    )
    list_filter = (
        'student',
        'question',
    )
    change_list_template = 'smuggler/change_list.html'
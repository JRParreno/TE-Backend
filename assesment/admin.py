from django.contrib import admin
from .models import Assesment


@admin.register(Assesment)
class AssesmentAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'activity',
        'student',
        'score',
        'date_taken',
    )
    list_filter = (
        'score',
        'date_taken',
    )
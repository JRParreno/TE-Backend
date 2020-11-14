from django.contrib import admin
from .models import Section, StudentSection

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'user',
        'code',
        'schedule',
    )
    list_filter = (
        'code',
        'user',
    )


@admin.register(StudentSection)
class SectionStudentAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'professor',
        'student',
        'section',
    )
    list_filter = (
        'student',
        'section',
    )
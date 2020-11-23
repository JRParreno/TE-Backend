from django.contrib import admin
from .models import Chapter, StudentRemarks, ChapterFeedback


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'filename',
        'embbeded_url',
        'note',
    )
    list_filter = (
        'filename',
    )
    change_list_template = 'smuggler/change_list.html'


@admin.register(ChapterFeedback)
class ChapteFeedbackAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'user',
        'student_chapter',
        'feedback',
        'date_posted',
    )
    list_filter = (
        'student_chapter',
        'user',
        'date_posted',
    )
    change_list_template = 'smuggler/change_list.html'


@admin.register(StudentRemarks)
class StudentRemarksAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'user',
        'chapter',
        'remarks',
    )
    list_filter = (
        'chapter',
    )
    change_list_template = 'smuggler/change_list.html'
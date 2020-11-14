from django.contrib import admin
from .models import Question, Choices, AnswerKey


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'number',
        'question_name',
        'q_type',
        'activity',
    )
    list_filter = (
        'activity',
        'q_type',
    )


@admin.register(Choices)
class ChoicesAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'get_chapter',
        'activity_code',
        'question',
        'description',
    )
    list_filter = (
        'question',
        'description',
        
    )


@admin.register(AnswerKey)
class AnswerAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'question',
        'answer',
    )
    list_filter = (
        'question',
        'answer',
        
    )
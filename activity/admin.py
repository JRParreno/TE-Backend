from django.contrib import admin
from .models import Activity, ProfActivity, ActivityRemarks


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'activity_name',
        'chapter',
    )
    list_filter = (
        'activity_name',
        'chapter',
    )

@admin.register(ProfActivity)
class ProfActivityAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'section',
        'activity',
        'start',
        'end',
        'remarks',
    )
    list_filter = (
        'section',
        'activity',
        'remarks',
    )


@admin.register(ActivityRemarks)
class ActivityRemarksAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'activity',
        'user',
        'remarks',
    )
    list_filter = (
        'activity',
        'user',
        'remarks',
    )
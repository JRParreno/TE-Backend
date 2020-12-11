from django.contrib import admin
from .models import Activity, ProfActivity, ActivityRemarks, ActivityType


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'activity_number',
        'pk',
        'activity_type',
        'activity_name',
        'chapter',
        'description'
    )
    list_filter = (
        'activity_type',
        'activity_name',
        'chapter',
    )

    change_list_template = 'smuggler/change_list.html'

@admin.register(ProfActivity)
class ProfActivityAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'pk',
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

    change_list_template = 'smuggler/change_list.html'


@admin.register(ActivityType)
class ActivityTypeAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'pk',
        'name',
    )
    list_filter = (
        'name',
    )

    change_list_template = 'smuggler/change_list.html'


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
    change_list_template = 'smuggler/change_list.html'
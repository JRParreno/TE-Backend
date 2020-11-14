# accounts.admin.py

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .models import User


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'username',
        'email',
        'last_name',
        'first_name',
        'middle_name',
        'university_id',
        'is_professor',
    )
    list_filter = (
        'username',
        'email',
        'last_name',
        'university_id',
        'is_professor',
    )
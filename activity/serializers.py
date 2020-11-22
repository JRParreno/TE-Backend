from rest_framework import serializers
from authentication.models import User
from sections.models import Section
from .models import Activity, ProfActivity, ActivityRemarks, ActivityType


class ActivitySerializer(serializers.ModelSerializer):
    
    activity_type = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'chapter', 'activity_name', 'activity_type', 'description']


class ProfActivitySerializer(serializers.ModelSerializer):
    activity_name = serializers.CharField(source='activity.activity_name', read_only=True)
    section_code = serializers.CharField(source='section.code', read_only=True)
    activity_type = serializers.CharField(source='activity.activity_type', read_only=True)
    chapter = serializers.IntegerField(source='activity.chapter.pk', read_only=True)
    description = serializers.ReadOnlyField(source='activity_description')
    
    class Meta:
        model = ProfActivity
        fields = ['id', 'chapter','activity', 'activity_name', 'activity_type', 'description', 'section', 'section_code', 'start', 'end', 'remarks']


class ActivityTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityType
        fields = ['id', 'name']

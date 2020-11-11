from rest_framework import serializers
from authentication.models import User
from sections.models import Section
from .models import Activity, ProfActivity, ActivityRemarks


class ActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Activity
        fields = ['id', 'activity_name', 'chapter']


class ProfActivitySerializer(serializers.ModelSerializer):
    activity_name = serializers.CharField(source='activity.activity_name', read_only=True)
    section_code = serializers.CharField(source='section.code', read_only=True)
    class Meta:
        model = ProfActivity
        fields = ['id', 'activity', 'activity_name', 'section', 'section_code', 'start', 'end', 'remarks']


# class StudentRemarksSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = StudentRemarks
#         fields = ['chapter', 'user', 'remarks']

#     def create(self, validated_data):
#         instance, _ = StudentRemarks.objects.get_or_create(**validated_data)
#         return instance


# class ChapterFeedbackSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ChapterFeedback
#         fields = ['user', 'student_chapter', 'feedback']

#     def create(self, validated_data):
#         print(validated_data)

#         return ChapterFeedback.objects.create(**validated_data)

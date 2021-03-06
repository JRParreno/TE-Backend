from rest_framework import serializers
from authentication.models import User
from sections.models import Section
from .models import Chapter, StudentRemarks, ChapterFeedback


class ChapterSerializer(serializers.ModelSerializer):
    filename = serializers.CharField(max_length=100, min_length=3)
    embbeded_url = serializers.CharField(max_length=255, min_length=3)
    note = serializers.CharField(max_length=255, min_length=3)

    class Meta:
        model = Chapter
        fields = ['id', 'filename', 'embbeded_url', 'note']


class StudentRemarksSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentRemarks
        fields = ['chapter', 'user', 'remarks']

    def create(self, validated_data):
        instance, _ = StudentRemarks.objects.get_or_create(**validated_data)
        return instance


class ChapterFeedbackSerializer(serializers.ModelSerializer):

    date_posted = serializers.DateTimeField(format='%m-%d-%Y' ,read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ChapterFeedback
        fields = ['user', 'username', 'student_chapter', 'feedback', 'date_posted']

    def create(self, validated_data):

        return ChapterFeedback.objects.create(**validated_data)

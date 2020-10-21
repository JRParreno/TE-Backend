from rest_framework import serializers
from authentication.models import User
from sections.models import Section
from .models import Chapter


class ChapterSerializer(serializers.ModelSerializer):
    filename = serializers.CharField(max_length=100, min_length=3)
    embbeded_url = serializers.CharField(max_length=255, min_length=3)
    note = serializers.CharField(max_length=255, min_length=3)

    class Meta:
        model = Chapter
        fields = ['id', 'filename', 'embbeded_url', 'note']

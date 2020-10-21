# from rest_framework import serializers
# from django.contrib.auth.models import User
# from sections.models import Section
# from .models import Chapter


# class ChapterSerializer(serializers.ModelSerializer):
#     section = serializers.PrimaryKeyRelatedField(read_only=True)
#     title = serializers.CharField(max_length=100, min_length=3)
#     description = serializers.CharField(max_length=255, min_length=3)
#     embbeded_url = serializers.CharField(max_length=255, min_length=3)
#     note = serializers.CharField(max_length=255, min_length=3)

#     class Meta:
#         model = Chapter
#         fields = ['title', 'description', 'embbeded_url', 'note', 'section']

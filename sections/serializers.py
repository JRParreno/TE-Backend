from rest_framework import serializers
from .models import Section, StudentSection


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ['id', 'user', 'code', 'schedule']


class SectionStudentSerializer(serializers.ModelSerializer):
    student_number = serializers.CharField(source='student.university_id', read_only=True)
    first_name = serializers.CharField(source='student.first_name', read_only=True)
    last_name = serializers.CharField(source='student.last_name', read_only=True)
    middle_name = serializers.CharField(source='student.middle_name', read_only=True)
    section_name = serializers.CharField(source='section.section_name', read_only=True)
    user_id = serializers.CharField(source='student.pk', read_only=True)
    
    class Meta:
        model = StudentSection
        fields = ['user_id', 'section_name', 'student_number', 'first_name', 'last_name', 'middle_name']

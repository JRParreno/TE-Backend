from rest_framework import serializers
from authentication.models import User
from sections.models import StudentSection


class AssesmentSerializer(serializers.ModelSerializer):
    
    # student_number = serializers.CharField(source='student.university_id',read_only=True)
    # full_name =serializers.ReadOnlyField()
    
    class Meta:
        model = StudentSection
        fields = ['section', 'student']

    
from rest_framework import serializers
from authentication.models import User
from .models import Assesment


class AssesmentSerializer(serializers.ModelSerializer):
    
    student_number = serializers.CharField(source='student.university_id',read_only=True)
    # first_name = serializers.CharField(source='student.first_name',read_only=True)
    # middle_name = serializers.CharField(source='student.middle_name',read_only=True)
    # last_name = serializers.CharField(source='student.last_name',read_only=True)
    get_full_name =serializers.SerializerMethodField
    
    class Meta:
        model = Assesment
        fields = ['activity', 'student', 'student_number','get_full_name','score', 'date_taken']

    def get_full_name(self, obj):
        return '{} {} {}'.format(obj.last_name, obj.first_name, obj.middle_name)
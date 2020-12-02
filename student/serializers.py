from rest_framework import serializers
from authentication.models import User
from sections.models import Section
from assesment.models import Assesment
from question.models import Question
from .models import SubmitSummary

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'university_id', 'first_name',
                  'middle_name', 'last_name', 'is_professor', 'email']


class AssesmentScoreSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Assesment
        fields = ['score']


class SubmitSerializer(serializers.ModelSerializer):

    code_file = serializers.FileField(required=False)
    table_image = serializers.ImageField(required=False)
    
    class Meta:
        model = SubmitSummary
        fields = ['id', 'question', 'student', 'answer', 'table_image', 'code_file']


class SubmitUpdateSerializer(serializers.ModelSerializer):

    code_file = serializers.FileField(required=False)
    table_image = serializers.ImageField(required=False)
    assesment = AssesmentScoreSerializer(source='question.activity', write_only=True)
    qestion_name = serializers.CharField(source='question.question_name', read_only=True)
    q_type = serializers.CharField(source='question.q_type')
    student = serializers.CharField(read_only=True)
    points = serializers.IntegerField(read_only=True)
    max_points = serializers.IntegerField(source='question.points', read_only=True)

    class Meta:
        model = SubmitSummary
        fields = ['id', 'question', 'q_type','qestion_name', 'max_points',
            'student', 'answer', 'table_image', 'code_file', 'assesment', 'points']

  
class SubmitSummarySerializer(serializers.ModelSerializer):

    submitsummary = SubmitUpdateSerializer(many=True, read_only=True)
    full_name = serializers.ReadOnlyField(source='student.full_name')
    student_number = serializers.CharField(source='student.university_id', read_only=True)
    student_id = serializers.CharField(source='student.pk', read_only=True)

    class Meta:
        model = Assesment
        fields = ['student_id','full_name', 'student_number', 'submitsummary']


class StudentSectionSerializer(serializers.ModelSerializer):

    full_name = serializers.ReadOnlyField(source='student.full_name', read_only=True)
    student_number = serializers.CharField(source='student.university_id', read_only=True)
    student_id = serializers.CharField(source='student.pk', read_only=True)
    class Meta:
        model = SubmitSummary
        fields = ['student_id', 'full_name', 'student_number']

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


class SubmitSummarySerializer(serializers.ModelSerializer):

    code_file = serializers.FileField(required=False)
    table_image = serializers.ImageField(required=False)
    assesment = AssesmentScoreSerializer(source='question.activity', write_only=True)
    qestion_name = serializers.CharField(source='question.question_name', read_only=True)
    q_type = serializers.CharField(source='question.q_type')

    class Meta:
        model = SubmitSummary
        fields = ['id', 'question', 'q_type','qestion_name', 'student', 'answer', 'table_image', 'code_file', 'assesment']



# class StudentUserSerializer(serializers.ModelSerializer):
#     # password = serializers.CharField(
#     #     max_length=65, min_length=8, write_only=True)
#     first_name = serializers.CharField(max_length=255, min_length=2)
#     last_name = serializers.CharField(max_length=255, min_length=2)
#     middle_name = serializers.CharField(max_length=255, min_length=2)

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name',
#                   'email', 'middle_name']


#     def create(self, validated_data):
#         student_number = validated_data.pop('username')
#         student_data = {
#             "username": student_number,
#             "password": student_number,
#             "email": validated_data.pop('email'),
#             "first_name": validated_data.pop('first_name'),
#             "last_name": validated_data.pop('last_name'),
#             "middle_name": validated_data.pop('middle_name'),
#             "university_id": student_number,
#         }
#         user = User.objects.create_user(**student_data)
#         get_user = User.objects.get(username=user)
#         section = Section.objects.get(pk=self.context['pk'])
#         StudentSection.objects.create(section=section, student=get_user)
#         return user

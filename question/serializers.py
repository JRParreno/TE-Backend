from rest_framework import serializers
from authentication.models import User
from sections.models import Section
from .models import Question, Choices


class QuestionViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'q_type', 'question_name', 'activity', 'number']


class ChoicesSerializer(serializers.ModelSerializer):
    question_name = serializers.CharField(source='question.question_name', read_only=True)
    class Meta:
        model = Choices
        fields = ['question', 'question_name', 'description']
    
    def create(self, validated_data):

        return Choices.objects.create(**validated_data)


class ChoiceTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = ['description']
    
    def create(self, validated_data):

        return Choices.objects.create(**validated_data)


class QuestionnaireSerializer(serializers.ModelSerializer):
    
    choices = ChoiceTextSerializer(many=True, read_only=True)
    answer = serializers.CharField(read_only=True)
    table_filename = serializers.CharField(read_only=True)
    
    class Meta:
        model = Question
        fields = ['number', 'id', 'q_type', 'question_name',
            'choices', 'answer', 'table_filename']




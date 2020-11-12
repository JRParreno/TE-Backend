from rest_framework import serializers
from authentication.models import User
from sections.models import Section
from .models import SubmitAnswer

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'university_id', 'first_name',
                  'middle_name', 'last_name', 'is_professor', 'email']



class SubmitSerializer(serializers.ModelSerializer):      
    
    class Meta:         
        model = SubmitAnswer         
        fields = ['user', 'question', 'description']          
    
    def create(self, validated_data):          
        return SubmitAnswer.objects.create(**validated_data)
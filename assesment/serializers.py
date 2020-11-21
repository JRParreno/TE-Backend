from rest_framework import serializers
from authentication.models import User
from .models import Assesment
from student.models import SubmitSummary


class AssesmentSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Assesment
        fields = ['activity', 'score', 'date_taken']


class AssesmentUserSerializer(serializers.ModelSerializer):
    full_name =serializers.ReadOnlyField()
    assesment = AssesmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['university_id' ,'full_name', 'assesment']
    
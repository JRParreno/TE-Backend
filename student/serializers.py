from rest_framework import serializers
from authentication.models import User
from sections.models import Section


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'university_id', 'first_name',
                  'middle_name', 'last_name', 'is_professor', 'email']

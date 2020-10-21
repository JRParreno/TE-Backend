from rest_framework import serializers
from .models import Section


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ['id', 'user', 'code', 'schedule']

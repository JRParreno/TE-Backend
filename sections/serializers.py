from rest_framework import serializers
from .models import Section
from django.contrib.auth.models import User


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ['user', 'code', 'schedule']

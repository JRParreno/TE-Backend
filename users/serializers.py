from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Professor


class ProfUpdateSerializer(serializers.ModelSerializer):
    middle_name = serializers.CharField(source='professor.middle_name')
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    middle_name = serializers.CharField(source='professor.middle_name')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'middle_name']

    def update(self, instance, validated_data):
        middle_name_data = validated_data.pop('professor')
        user = User.objects.filter(username=instance).update(**validated_data)

        Professor.objects.update(user=instance, **middle_name_data)
        print(middle_name_data['middle_name'])
        return instance

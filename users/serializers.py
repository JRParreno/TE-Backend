from authentication.models import User
from rest_framework import serializers


# Professor update serializer
class ProfUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    middle_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'middle_name']

    def update(self, instance, validated_data):
        user = User.objects.filter(username=instance).update(**validated_data)
        return instance


# Student update serializer
class StudentUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    middle_name = serializers.CharField(max_length=255, min_length=2)
    university_id = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'university_id', 'email', 'first_name',
                  'last_name', 'middle_name']

    def update(self, instance, validated_data):
        user = User.objects.filter(username=instance).update(**validated_data)
        print(validated_data)
        return instance

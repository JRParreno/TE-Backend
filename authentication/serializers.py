
from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Professor


class ProfessorSerializer(serializers.ModelSerializer):

    faculty_id = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = Professor
        fields = ['faculty_id']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    professor = serializers.CharField(source='professor.faculty_id')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'professor']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        professor_data = validated_data.pop('professor')
        user = User.objects.create_user(**validated_data)
        user.save()
        Professor.objects.create(user=user, **professor_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']

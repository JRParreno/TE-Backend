from django.shortcuts import render
from .serializers import AssesmentSerializer, AssesmentUserSerializer
from .models import Assesment
from rest_framework import status, views, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from sections.models import StudentSection
from authentication.models import User


# activity type
class AssesmentAPIView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AssesmentUserSerializer

    def get_queryset(self):
        section = self.kwargs['section']
        return User.objects.all().order_by('last_name')

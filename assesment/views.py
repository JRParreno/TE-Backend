from django.shortcuts import render, get_object_or_404
from .serializers import AssesmentSerializer, AssesmentUserSerializer
from .models import Assesment
from rest_framework import status, views, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from sections.models import StudentSection
from authentication.models import User


class AssesmentAPIView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AssesmentUserSerializer

    def get_queryset(self):
        students = None
        if self.request.user.is_professor:
            section = StudentSection.objects.filter(section__user=self.request.user).values('student')
            students = User.objects.filter(id__in=section).order_by('last_name')
            
        return students

class AssesmentFilterAPIView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AssesmentUserSerializer

    def get_queryset(self):
        section = self.kwargs['section']
        students = None
        if self.request.user.is_professor:
            student_section = StudentSection.objects.filter(section=section).values('student')
            students = User.objects.filter(id__in=student_section)
        return students
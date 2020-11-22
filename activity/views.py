from django.shortcuts import render
from .serializers import ActivitySerializer, ProfActivitySerializer, ActivityTypeSerializer
# from .permissions import IsProfessor
from .models import Activity, ProfActivity, ActivityRemarks, ActivityType
from rest_framework import status, views, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from sections.models import StudentSection
from rest_framework.views import APIView

# activity viewset
class ActivityViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return self.queryset.filter(activity_type=self.kwargs['activity_type'])

# activity viewset for professor
class ProfActivityViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProfActivity.objects.all()
    serializer_class = ProfActivitySerializer

    def get_queryset(self):
        queryset = self.queryset.filter(activity__activity_type=self.kwargs['activity_type'], section__user=self.request.user)
        return queryset


# activity viewset for professor
class StudentActivityAPIView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProfActivity.objects.all()
    serializer_class = ProfActivitySerializer

    def get_queryset(self):
        queryset = None

        if not self.request.user.is_professor:
            section = StudentSection.objects.get(student=self.request.user)
            queryset = self.queryset.filter(activity__activity_type=self.kwargs['activity_type'], section=section.section)

        return queryset


# activity type
class ActivityTypeAPIView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer

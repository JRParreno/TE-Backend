from django.shortcuts import render
from .serializers import ActivitySerializer, ProfActivitySerializer, ActivityTypeSerializer
# from .permissions import IsProfessor
from .models import Activity, ProfActivity, ActivityRemarks, ActivityType
from rest_framework import status, views, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

# activity viewset for professor
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
        return self.queryset.filter(activity__activity_type=self.kwargs['activity_type'])


# activity viewset for professor
class ActivityTypeAPIView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer

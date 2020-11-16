from django.shortcuts import render
from .serializers import ActivitySerializer, ProfActivitySerializer
# from .permissions import IsProfessor
from .models import Activity, ProfActivity, ActivityRemarks
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


# activity viewset for professor
class ProfActivityViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProfActivity.objects.all()
    serializer_class = ProfActivitySerializer

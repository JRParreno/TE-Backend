from django.shortcuts import render
from .serializers import AssesmentSerializer
from .models import Assesment
from rest_framework import status, views, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from sections.models import StudentSection

# activity type
class AssesmentAPIView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    #queryset = Assesment.objects.all()
    serializer_class = AssesmentSerializer

    def get_queryset(self):
        section = self.kwargs['section']
        return Assesment.objects.all().order_by('activity')

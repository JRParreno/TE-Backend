from django.shortcuts import render
from .serializers import ActivitySerializer, ProfActivitySerializer
# from .permissions import IsProfessor
from .models import Activity, ProfActivity, ActivityRemarks
from rest_framework import status, views, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets


# chapter viewset for professor
class ActivityViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


# chapter viewset for professor
class ProfActivityViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProfActivity.objects.all()
    serializer_class = ProfActivitySerializer

# class ChapterFeedbackAPIView(generics.ListCreateAPIView):

#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = ChapterFeedbackSerializer
#     queryset = ChapterFeedback.objects.all()

#     def get_queryset(self):  # filter by chapter
#         return self.queryset.filter(student_chapter=self.kwargs['chapter'])

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class StudentRemarksAPIView(generics.ListCreateAPIView):

#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = StudentRemarksSerializer
#     queryset = StudentRemarks.objects.all()

#     def get_queryset(self):  # filter by section
#         return self.queryset.filter(user__section=self.kwargs['section'])

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

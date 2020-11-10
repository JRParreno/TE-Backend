from django.shortcuts import render, get_object_or_404
from .serializers import SectionSerializer, SectionStudentSerializer
from .models import Section, StudentSection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, views, permissions, generics
from rest_framework import permissions
from authentication.models import User
from rest_framework import viewsets
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from authentication.serializers import StudentUserSerializer
from rest_framework.generics import GenericAPIView

# section apiview


class SectionAPIView(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    # def list(self, request):  # get method
    #     queryset = Section.objects.all()
    #     serializer = SectionSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request):  # post method
    #     serializer = SectionSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):  # get method
    #     queryset = Section.objects.all()
    #     section = get_object_or_404(queryset, pk=pk)
    #     serializer = SectionSerializer(section)

    #     return Response(serializer.data)

    # def update(self, request, pk=None):  # put method
    #     section = Section.objects.get(pk=pk)
    #     serializer = SectionSerializer(section, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk):

    #     section = self.get_object(pk)
    #     section.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class StudentSectionAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StudentUserSerializer
    
    
    def get(self, request, *args, **kwargs):
        students = StudentSection.objects.filter(section=self.kwargs['pk'], student__is_professor=False)
        serializer = SectionStudentSerializer(students, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = StudentUserSerializer(data=request.data, context={'pk': self.kwargs['pk']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

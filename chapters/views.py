from django.shortcuts import render
from .serializers import ChapterSerializer
from .models import Chapter
from sections.models import Section
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# chapter apiview
class ChapterAPIView(APIView):

    def get(self, request):
        chapters = Chapter.objects.all()
        serializer = ChapterSerializer(chapters, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChapterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

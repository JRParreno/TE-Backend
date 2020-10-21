from django.shortcuts import render
from .serializers import ChapterSerializer
from .models import Chapter
# from .permissions import IsProfessor
from sections.models import Section
from rest_framework import status, views, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets


# chapter viewset for professor
class ChapterAPIView(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    lookup_field = "id"
    # def get(self, request):
    #     chapters = Chapter.objects.all()
    #     serializer = ChapterSerializer(chapters, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = ChapterSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

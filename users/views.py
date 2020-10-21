from django.shortcuts import render, get_object_or_404
from rest_framework import generics, mixins, permissions
from .serializers import ProfUpdateSerializer, StudentUpdateSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

# professor udpate profile
# GET, PUT and PATCH method


class ProfUpdateView(generics.RetrieveUpdateAPIView):

    serializer_class = ProfUpdateSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


# student update profile
# GET, PUT and PATCH method
class StudentUpdateView(generics.RetrieveUpdateAPIView):

    serializer_class = StudentUpdateSerializer

    def retrieve(self, request, *args, **kwargs):

        if User.objects.filter(username=self.kwargs.get("username")).exists():
            user = User.objects.get(username=self.kwargs.get("username"))
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'error': 'no user found'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):

        if User.objects.filter(username=self.kwargs.get("username")).exists():
            user = User.objects.get(username=self.kwargs.get("username"))
            serializer = self.serializer_class(
                user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'error': 'no user found'}, status=status.HTTP_400_BAD_REQUEST)

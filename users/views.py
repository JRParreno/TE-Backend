from django.shortcuts import render, get_object_or_404
from rest_framework import generics, mixins, permissions
from .serializers import ProfUpdateSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


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

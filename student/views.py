from django.shortcuts import render
from .serializers import StudentSerializer, SubmitSerializer
from authentication.models import User
from sections.models import Section
from rest_framework import status, views, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import SubmitAnswer
from activity.models import ActivityRemarks, Activity


class StudentViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.filter(is_professor=False)
    serializer_class = StudentSerializer


class SubmitAPIView(generics.CreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SubmitSerializer
    queryset = SubmitAnswer.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = request.user
        activity = Activity.objects.get(pk=self.kwargs['activity'])
        ActivityRemarks.objects.create(activity=activity, user=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

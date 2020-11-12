from django.shortcuts import render
# from .permissions import IsProfessor
from rest_framework import generics, permissions, status, views, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Question, Choices
from .serializers import QuestionnaireSerializer, ChoicesSerializer, QuestionViewSetSerializer

# chapter viewset for professor
class QuestionViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Question.objects.all()
    serializer_class = QuestionViewSetSerializer


# class ChoicesViewSet(viewsets.ModelViewSet):

#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Choices.objects.all()
#     serializer_class = QuestionSerializer


class QuestionAPIView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = QuestionnaireSerializer
    queryset = Question.objects.all()

    def get_queryset(self):  # filter by chapter
        return self.queryset.filter(activity=self.kwargs['activity'])


class ChoicesAPIView(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChoicesSerializer
    queryset = Choices.objects.all()

    def get_queryset(self):  # filter by chapter
        return self.queryset.filter(question__activity=self.kwargs['activity'])

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


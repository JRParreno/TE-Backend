from django.shortcuts import render
from .serializers import StudentSerializer, SubmitSerializer
from authentication.models import User
from sections.models import Section
from rest_framework import status, views, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from activity.models import ActivityRemarks, Activity
from question.models import Question
from assesment.models import Assesment
from activity.models import ActivityRemarks
from rest_framework.generics import GenericAPIView
import json 

class StudentViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.filter(is_professor=False)
    serializer_class = StudentSerializer



class SubmitAPIView(GenericAPIView):
    serializer_class = SubmitSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        answer_list = json.dumps(request.data)
        answer_dict = json.loads(answer_list)
        global score 
        score = 0
        for i in request.data:
            check = Question.objects.filter(pk=i['question'], answer=i['answer'])
            if check.exists():
                score +=1
        try:
            activity = Activity.objects.get(pk=self.kwargs['activity'])
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        ActivityRemarks.objects.create(activity=activity, user=request.user)
        Assesment.objects.create(activity=activity, student=request.user, score=score)
        
        return Response(serializer.data, status=status.HTTP_200_OK)



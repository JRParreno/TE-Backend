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
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.generics import GenericAPIView
from django.db.models import Q
import json 

class StudentViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.filter(is_professor=False)
    serializer_class = StudentSerializer



class SubmitAPIView(GenericAPIView):
    serializer_class = SubmitSerializer
    parser_classes = (MultiPartParser, FormParser,)
    
    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # answer_list = json.dumps(request.data)
        # answer_dict = json.loads(answer_list)
        # global score 
        # score = 0
        # for i in request.data:
        #     check = Question.objects.filter(Q(q_type__="IDENT") | Q(q_type="MULT"), pk=i['question'], answer=i['answer'])
        #     if check.exists():
        #         get_point = check.first()
        #         score += get_point.points
        # try:
        #     activity = Activity.objects.get(pk=self.kwargs['activity'])
        # except:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # ActivityRemarks.objects.create(activity=activity, user=request.user)
        # Assesment.objects.create(activity=activity, student=request.user, score=score)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)



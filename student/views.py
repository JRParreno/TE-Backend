from django.shortcuts import render, get_object_or_404
from .serializers import StudentSerializer, SubmitSerializer, SubmitSummarySerializer, SubmitUpdateSerializer
from authentication.models import User
from sections.models import Section
from rest_framework import status, views, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from activity.models import ActivityRemarks, Activity
from question.models import Question
from assesment.models import Assesment
from activity.models import ActivityRemarks, ActivityType
from sections.models import Section, StudentSection
from sections.models import Section, StudentSection
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.generics import GenericAPIView
from django.db.models import Q, F
from .models import SubmitSummary
import json 

class StudentViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.filter(is_professor=False)
    serializer_class = StudentSerializer



class SubmitAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SubmitSerializer
    parser_classes = (MultiPartParser, FormParser,)
    
    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            activity = Activity.objects.get(pk=self.kwargs['activity'])
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

        if len(request.FILES) == 0:
            answer_list = json.dumps(request.data)
            answer_dict = json.loads(answer_list)

            check_assesment = SubmitSummary.objects.filter(student=request.user, question=answer_dict['question'])
            
            if check_assesment.exists():
                data = {
                    'details': 'student already done this question'
                }
                return Response(data, status=status.HTTP_200_OK)

            
            check = Question.objects.filter(id=answer_dict['question'], answer=answer_dict['answer'])
            assesment = None
            assesment = Assesment.objects.filter(activity=activity, student=request.user)
            summary = serializer.save()
            if check.exists():
                
                if not assesment.exists():
                    created_assesment = Assesment.objects.create(activity=activity, student=request.user, score=1)
                    summary.assesment = created_assesment
                    summary.save()
                else:
                    assesment.update(score=F('score')+1)
                    get_assesment = Assesment.objects.get(pk=assesment.first().pk)
                    summary.assesment = get_assesment
                    summary.save()
            else:
                if not assesment.exists():
                    created_assesment = Assesment.objects.create(activity=activity, student=request.user, score=0)
                    summary.assesment = created_assesment
                    summary.save()
                else:
                    get_assesment = Assesment.objects.get(pk=assesment.first().pk)
                    summary.assesment = get_assesment
                    summary.save()

        else:
            assesment = Assesment.objects.filter(activity=activity, student=request.user)
            summary = serializer.save()
            if not assesment.exists():
                created_assesment = Assesment.objects.create(activity=activity, student=request.user, score=1)
                summary.assesment = created_assesment
                summary.save()
            else:
                get_assesment = Assesment.objects.get(pk=assesment.first().pk)
                summary.assesment = get_assesment
                summary.save()
            
        check_remarks(request, activity)
        
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class AssesmentUpdateAPIView(GenericAPIView):

    permission_classes=(permissions.IsAuthenticated,)
    serializer_class = SubmitUpdateSerializer
    
    def get(self, request, *args, **kwargs):
        activity = self.kwargs['activity']
        student = get_object_or_404(User, pk=self.kwargs['student_id'])
        queryset = SubmitSummary.objects.filter(student=student, question__activity=activity).order_by('student')
        serializer = SubmitSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        try:
            activity = Activity.objects.get(pk=self.kwargs['activity'])
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer = SubmitUpdateSerializer(data=request.data, many=True)
        answer_list = json.dumps(request.data)
        answer_dict = json.loads(answer_list)
        
        for k in answer_dict:
            if k['q_type'] != "MULT" or k['q_type'] != "IDENT":
                get_student = get_object_or_404(User, pk=self.kwargs['student_id'])
                check = Question.objects.filter(id=k['question'])
                if check.exists():
                    assesment = Assesment.objects.filter(activity=activity, student=get_student)

                    if not assesment.exists():
                        Assesment.objects.create(activity=activity, student=get_student, score=k['assesment']['score'])
                    else:
                        assesment.update(score=F('score')+k['assesment']['score'])
        
        check_remarks(request, activity)
        
        return Response(request.data, status=status.HTTP_200_OK)


def check_remarks(request, activity):

    submitted = SubmitSummary.objects.filter(student=request.user, question__activity=activity).count()
    total_question = Question.objects.filter(activity=activity).count()

        
    if submitted is total_question:
        ActivityRemarks.objects.create(activity=activity, user=request.user)


class StudentSubmitListAPIView(generics.ListAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    serializer_class = SubmitSummarySerializer

    def get_queryset(self):
        get_student_section = StudentSection.objects.filter(section=self.kwargs['section']).values('student')
        activity_type = get_object_or_404(ActivityType, name="Laboratory")
        students = Assesment.objects.filter(student__in=get_student_section, activity=self.kwargs['activity'], activity__activity_type=activity_type)
        return students
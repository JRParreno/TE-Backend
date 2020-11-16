from django.shortcuts import render
from .serializers import ActivitySerializer, ProfActivitySerializer
# from .permissions import IsProfessor
from .models import Activity, ProfActivity, ActivityRemarks
from rest_framework import status, views, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

# activity viewset for professor
class ActivityViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


# activity viewset for professor
class ProfActivityViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProfActivity.objects.all()
    serializer_class = ProfActivitySerializer

    # def retrieve(self, request, pk=None):
    #     try:
    #         activity = ProfActivity.objects.get(activity=self.kwargs['pk'], student__is_professor=False)
    #         serializer = ProfActivitySerializer(activity, many=True)

    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

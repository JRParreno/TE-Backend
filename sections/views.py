# from django.shortcuts import render
# from .serializers import SectionSerializer
# from .models import Section
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView


# # section apiview
# class SectionAPIView(APIView):

#     def get(self, request):
#         sections = Section.objects.all()
#         serializer = SectionSerializer(sections, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = SectionSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

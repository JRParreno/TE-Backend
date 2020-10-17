from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer, StudentUserSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
import jwt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

# Register for Professor


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Register for Student
class StudentRegisterView(GenericAPIView):
    serializer_class = StudentUserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(StudentRegisterView, self).get_permissions()

    def post(self, request):
        serializer = StudentUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            res = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            # auth_token = jwt.encode(
            #     {'username': user.username}, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': res}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

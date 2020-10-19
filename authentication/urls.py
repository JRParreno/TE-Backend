from django.urls import path
from .views import (RegisterView, LoginView,
                    StudentRegisterView,
                    PasswordTokenCheckAPI,
                    RequestPasswordResetEmail,
                    SetNewPasswordAPIView)


urlpatterns = [
    path('professor/register', RegisterView.as_view()),
    path('professor/login', LoginView.as_view()),
    path('student/register', StudentRegisterView.as_view()),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
]

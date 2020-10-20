from django.urls import path
from .views import (ProfRegisterView, ProfLoginView,
                    StudentRegisterView,
                    StudebtLoginView,
                    PasswordTokenCheckAPI,
                    RequestPasswordResetEmail,
                    SetNewPasswordAPIView,
                    ChangePasswordView)


urlpatterns = [
    path('professor/register/', ProfRegisterView.as_view()),
    path('professor/login/', ProfLoginView.as_view()),
    path('student/register/', StudentRegisterView.as_view()),
    path('student/login/', StudebtLoginView.as_view()),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email/"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
    path('change-password/', ChangePasswordView.as_view(),
         name='change-password'),
]

from django.urls import path
from .views import RegisterView, LoginView, StudentRegisterView


urlpatterns = [
    path('professor/register', RegisterView.as_view()),
    path('professor/login', LoginView.as_view()),
    path('student/register', StudentRegisterView.as_view()),
]

from django.urls import path
from .views import RegisterView, LoginView


urlpatterns = [
    path('professor/register', RegisterView.as_view()),
    path('professor/login', LoginView.as_view()),
]

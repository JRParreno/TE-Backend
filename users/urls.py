from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from .views import ProfUpdateView, StudentUpdateView


urlpatterns = [
    path('profile/professor/<username>/', ProfUpdateView.as_view()),
    path('profile/student/<username>/', StudentUpdateView.as_view()),
]

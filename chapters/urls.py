from django.urls import path, include
from .views import ChapterViewSet, ChapterFeedbackAPIView, StudentRemarksAPIView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('list', ChapterViewSet, basename='chapter')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('feedback/<chapter>/', ChapterFeedbackAPIView.as_view()),
    path('complete/<section>/', StudentRemarksAPIView.as_view()),
]

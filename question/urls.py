from django.urls import path, include
from .views import QuestionViewSet, ChoicesAPIView, QuestionAPIView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('list', QuestionViewSet, basename='question')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('list/activity/<activity>/', ChoicesAPIView.as_view()),
    path('list/<activity>/', QuestionAPIView.as_view()),
    # path('complete/<section>/', StudentRemarksAPIView.as_view()),
]

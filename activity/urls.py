from django.urls import path, include
from .views import ActivityViewSet, StudentActivityAPIView,ProfActivityViewSet, ActivityTypeAPIView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('list', ActivityViewSet, basename='activity')
router.register('prof_activity', ProfActivityViewSet, basename='activity')

urlpatterns = [
    path('viewset/<int:activity_type>/', include(router.urls)),
    path('viewset/<int:activity_type>/<int:pk>/', include(router.urls)),
    path('type/', ActivityTypeAPIView.as_view()),
    path('student/<int:activity_type>/', StudentActivityAPIView.as_view()),
]

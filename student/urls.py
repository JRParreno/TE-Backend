from django.urls import path, include
from .views import StudentViewSet, SubmitAPIView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('list', StudentViewSet, basename='student')


app_name = 'student'
urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('submit/<activity>/', SubmitAPIView.as_view()),
]


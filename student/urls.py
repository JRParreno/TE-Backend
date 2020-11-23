from django.urls import path, include
from .views import StudentViewSet, StudentSectionListAPIView, SubmitAPIView, AssesmentUpdateAPIView, StudentSubmitListAPIView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('list', StudentViewSet, basename='student')


app_name = 'student'
urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('submit/<int:activity>/', SubmitAPIView.as_view()),
    path('update/<int:student_id>/<int:activity>/', AssesmentUpdateAPIView.as_view()),
    path('summary/<int:section>/<int:activity>/', StudentSubmitListAPIView.as_view()),
    path('section/list/<int:section>/', StudentSectionListAPIView.as_view()),
]


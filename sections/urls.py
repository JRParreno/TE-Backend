from django.urls import path, include
from .views import SectionAPIView, StudentSectionAPIView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('list', SectionAPIView, basename='section')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('students/<int:pk>/', StudentSectionAPIView.as_view())
]

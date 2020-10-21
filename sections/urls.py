from django.urls import path, include
from .views import SectionAPIView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('list', SectionAPIView, basename='section')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]

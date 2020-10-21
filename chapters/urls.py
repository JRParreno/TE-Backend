from django.urls import path, include
from .views import ChapterAPIView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('list', ChapterAPIView, basename='chapter')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]

from django.urls import path, include
from .views import ActivityViewSet, ProfActivityViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('list', ActivityViewSet, basename='activity')
router.register('prof_activity', ProfActivityViewSet, basename='activity')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]

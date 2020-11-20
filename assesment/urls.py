from django.urls import path, include
from .views import AssesmentAPIView

urlpatterns = [
    # path('list/<int:section>/<int:activity_type>/<int:activity>/'
    #     , AssesmentAPIView.as_view()),
    path('list/'
        , AssesmentAPIView.as_view()),
]

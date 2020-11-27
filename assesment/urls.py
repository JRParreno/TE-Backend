from django.urls import path, include
from .views import AssesmentAPIView, AssesmentFilterAPIView, AssesmentActivityStudentAPIView

urlpatterns = [
    # path('list/<int:section>/<int:activity_type>/<int:activity>/'
    #     , AssesmentAPIView.as_view()),
    path('list/'
        , AssesmentAPIView.as_view()),
    path('list/filter/<section>/'
        , AssesmentFilterAPIView.as_view()),
    path('activity/', AssesmentActivityStudentAPIView.as_view())
]

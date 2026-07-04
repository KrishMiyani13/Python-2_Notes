from django.urls import path
from students.views import CourseListCreateAPIView,StudentListCreateAPIView,CourseRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('courses/',CourseListCreateAPIView.as_view(),name="api_course_list_create"),
    path('students/',StudentListCreateAPIView.as_view(),name="api_student_list_create"),
    path('courses/<int:pk>/',CourseRetrieveUpdateDestroyAPIView.as_view(),name="course_details"),
]
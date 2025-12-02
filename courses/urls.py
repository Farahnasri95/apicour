from django.urls import path
from . import views

urlpatterns = [
    path('course/add/', views.add_course),
    path('course/update/<int:course_id>/', views.update_course),
    path('course/delete/<int:course_id>/', views.delete_course),
    path('course/list/', views.list_courses),
    path('course/search/', views.search_courses),
    path('course/enroll/', views.enroll_student),
    path('course/<int:course_id>/', views.course_detail),
    path('studentcourses/<int:student_id>/', views.student_courses_ids),
]

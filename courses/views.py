from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models
from .models import Course, StudentCourse
from .serializers import CourseSerializer, StudentCourseSerializer

# ---------- Course CRUD ----------
@api_view(['POST'])
def add_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Course added successfully"})
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=404)

    serializer = CourseSerializer(course, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Course updated successfully"})
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        course.delete()
        return Response({"message": "Course deleted successfully"})
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=404)


@api_view(['GET'])
def list_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_courses(request):
    query = request.GET.get('q', '')
    courses = Course.objects.filter(
        models.Q(name__icontains=query) |
        models.Q(instructor__icontains=query) |
        models.Q(category__icontains=query)
    )
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def course_detail(request, course_id):
    """
    Retourne les détails d'un cours à partir de son id
    """
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=404)

    serializer = CourseSerializer(course)
    return Response(serializer.data)
@api_view(['GET'])
def student_courses_ids(request, student_id):
    student_courses = StudentCourse.objects.filter(student_id=student_id)
    serializer = StudentCourseSerializer(student_courses, many=True)
    return Response(serializer.data)
# ---------- Enrollments ----------
@api_view(['POST'])
def enroll_student(request):
    serializer = StudentCourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student enrolled successfully"})
    return Response(serializer.errors, status=400)

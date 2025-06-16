from django.shortcuts import render
from .models import Course
# Create your views here.

def view_courses(request):
    courses = Course.objects.prefetch_related('modules').all()
    return render(request, 'view_course.html', {'courses': courses})
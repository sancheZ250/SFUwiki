from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Institute, Department, Teacher, Discipline, Review
from .serializers import InstituteSerializer, DepartmentSerializer, TeacherSerializer, DisciplineSerializer, \
    ReviewSerializer


def index(request):
    return HttpResponse("Hello world!")


#API-view
class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class TeacherReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        teacher_id = self.kwargs.get('teacher_id')
        return Review.objects.filter(teacher_id=teacher_id)


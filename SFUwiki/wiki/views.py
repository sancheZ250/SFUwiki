from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from .models import Institute, Department, Teacher, Discipline, Review
from .serializers import InstituteSerializer, DepartmentSerializer, TeacherSerializer, DisciplineSerializer, \
    ReviewSerializer, TeacherNameAndPhotoSerializer, InstituteWithoutPhotoSerializer, SimpleDisciplineSerializer


def index(request):
    return HttpResponse("Hello world!")


class TeachersByDepartmentList(generics.ListAPIView):
    serializer_class = TeacherNameAndPhotoSerializer

    def get_queryset(self):
        department_id = self.kwargs['department_id']
        return Teacher.objects.filter(department_id=department_id)
# API-view:


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return SimpleDisciplineSerializer
        return DisciplineSerializer
class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return InstituteWithoutPhotoSerializer
        # Для всех остальных действий используем InstituteSerializer
        return InstituteSerializer



class DepartmentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        institute_id = self.kwargs['institute_pk']
        return Department.objects.filter(institute_id=institute_id)
    serializer_class = DepartmentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        institute_id = self.kwargs['institute_pk']
        return Teacher.objects.filter(institute_id=institute_id)

    #serializer_class = TeacherSerializer
    def get_serializer_class(self):
        # Если выполняется действие "list" (получение списка), используем TeacherNameAndPhotoSerializer
        if self.action == 'list':
            return TeacherNameAndPhotoSerializer
        # Для всех остальных действий используем TeacherSerializer
        return TeacherSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class TeacherReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        teacher_id = self.kwargs.get('teacher_id')
        return Review.objects.filter(teacher_id=teacher_id)


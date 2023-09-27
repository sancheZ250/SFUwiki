from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Institute, Department, Teacher
from .serializers import InstituteSerializer, DepartmentSerializer, TeacherSerializer


def index(request):
    return HttpResponse("Hello world!")


#API-view

class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


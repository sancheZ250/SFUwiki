from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.pagination import PageNumberPagination

from SFUwiki.pagination import AllTeacherPagination
from .models import Institute, Department, Teacher, Discipline, Review
from .permissions import IsAdminOrReadOnly, IsAdminOrAuthor, IsSuperUser, IsCommentAuthor
from .serializers import InstituteSerializer, DepartmentSerializer, TeacherSerializer, DisciplineSerializer, \
    ReviewSerializer, TeacherCardSerializer, InstituteWithoutPhotoSerializer, SimpleDisciplineSerializer, \
    SimpleDepartmentSerializer, ModerTeacherSerializer


class TeachersByDepartmentList(generics.ListAPIView):
    serializer_class = TeacherCardSerializer

    def get_queryset(self):
        department_id = self.kwargs['department_id']
        return Teacher.objects.select_related('department').filter(department_id=department_id)


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
        return InstituteSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        institute_id = self.kwargs['institute_pk']
        return Department.objects.select_related('institute').filter(institute_id=institute_id)

    def get_serializer_class(self):
        if self.action == 'list':
            return SimpleDepartmentSerializer
        return DepartmentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrAuthor]

    def get_queryset(self):
        institute_id = self.kwargs['institute_pk']
        if self.action == 'list':
            return Teacher.objects.prefetch_related('photos').filter(institute_id=institute_id, is_published=True)
        return Teacher.objects.select_related('institute').prefetch_related('photos').filter(institute_id=institute_id, is_published=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherCardSerializer
        return TeacherSerializer


class ModerTeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperUser]

    def get_queryset(self):
        institute_id = self.kwargs['institute_pk']
        return Teacher.objects.filter(institute_id=institute_id, is_published=False)

    def get_serializer_class(self):
        return ModerTeacherSerializer


# class TeacherReviewViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAdminOrAuthor]
#     serializer_class = ReviewSerializer
#
#     def get_queryset(self):
#         teacher_id = self.kwargs.get('teacher_id')
#         return Review.objects.filter(teacher_id=teacher_id)
class TeacherReviewList(ListCreateAPIView):
    permission_classes = [IsCommentAuthor]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        return Review.objects.filter(teacher_id=teacher_id)

    def perform_create(self, serializer):
        teacher_id = self.kwargs['teacher_id']
        serializer.save(teacher_id=teacher_id)


class TeacherReviewDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCommentAuthor]
    serializer_class = ReviewSerializer
    lookup_field = 'id'

    def get_queryset(self):
        review_id = self.kwargs['id']
        teacher_id = self.kwargs['teacher_id']
        return Review.objects.filter(teacher_id=teacher_id, id=review_id)


class AllTeachersAPIView(ListCreateAPIView):
    pagination_class = AllTeacherPagination
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TeacherCardSerializer
        return TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.filter(is_published=True)

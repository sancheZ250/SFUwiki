from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q, Prefetch
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from SFUwiki.pagination import AllTeacherPagination
from .models import Institute, Department, Teacher, Discipline, Review, TeacherPhoto
from .permissions import IsAdminOrReadOnly, IsAdminOrAuthor, IsSuperUser, IsCommentAuthor
from .serializers import InstituteSerializer, DepartmentSerializer, TeacherSerializer, DisciplineSerializer, \
    ReviewSerializer, TeacherCardSerializer, InstituteWithoutPhotoSerializer, SimpleDisciplineSerializer, \
    SimpleDepartmentSerializer, ModerTeacherSerializer, InstituteDepartmentSerializer, TeacherPhotoSerializer


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
    def get_queryset(self):
        if self.action == 'list':
            return Institute.objects.all()
        return Institute.objects.all().prefetch_related('departments').prefetch_related('photos')

    def get_serializer_class(self):
        if self.action == 'list':
            return InstituteWithoutPhotoSerializer
        return InstituteSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        institute_id = self.kwargs['institute_pk']
        if self.action == 'list':
            return Department.objects.filter(institute_id=institute_id)
        else:
            department_id = self.kwargs['pk']
            return Department.objects.filter(institute_id=institute_id, id=department_id).select_related('institute').prefetch_related('teachers')

    def get_serializer_class(self):
        if self.action == 'list':
            return SimpleDepartmentSerializer
        return DepartmentSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        teachers = instance.teachers.filter(is_published=True)
        serialized_data = DepartmentSerializer(instance, context=self.get_serializer_context()).data
        serialized_data['teachers'] = TeacherCardSerializer(teachers, many=True, context=self.get_serializer_context()).data
        return Response(serialized_data, status=status.HTTP_200_OK)


class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrAuthor]

    def get_queryset(self):
        institute_id = self.kwargs['institute_pk']
        if self.action == 'list':
            return Teacher.objects.prefetch_related('photos').filter(institute_id=institute_id, is_published=True)
        return Teacher.objects.select_related('institute').prefetch_related(
            'photos', Prefetch('reviews', queryset=Review.objects.select_related('student'))
            ).prefetch_related('disciplines').filter(institute_id=institute_id, is_published=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherCardSerializer
        return TeacherSerializer

    def perform_create(self, serializer):
        institute_id = self.request.data.get('institute_id')
        department_id = self.request.data.get('department_id')
        serializer.save(institute_id=institute_id, department_id=department_id)


class ModerTeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperUser]
    pagination_class = AllTeacherPagination
    queryset = Teacher.objects.filter(is_published=False)
    serializer_class = ModerTeacherSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherCardSerializer
        return ModerTeacherSerializer


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
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TeacherCardSerializer
        return TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.filter(is_published=True)


class InstituteDepartmentsAPIView(ListCreateAPIView):
    serializer_class = InstituteDepartmentSerializer
    queryset = Institute.objects.all()


class TeacherPhotoUploadView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherPhotoSerializer
    queryset = TeacherPhoto.objects.all()


def check_user_teacher_review(request):
    teacher_id = request.GET.get('teacherID')
    student_id = request.GET.get('studentID')
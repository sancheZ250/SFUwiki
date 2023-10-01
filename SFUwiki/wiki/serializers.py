from rest_framework import serializers
from .models import Institute, InstitutePhoto, Department, Teacher, TeacherPhoto


class InstitutePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutePhoto
        fields = ('photo',)


class TeacherPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherPhoto
        fields = '__all__'


class InstituteSerializer(serializers.ModelSerializer):
    photos = InstitutePhotoSerializer(many=True)

    class Meta:
        model = Institute
        fields = ('id', 'name', 'description', 'abbreviation', 'logo', 'photos',)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    photos = TeacherPhotoSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ('name', 'department', 'alma_mater', 'knowledge_rating', 'teaching_skill_rating', 'easiness_rating',
                  'communication_rating', 'institute', 'bio', 'photos')

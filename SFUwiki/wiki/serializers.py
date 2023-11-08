from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Institute, InstitutePhoto, Department, Teacher, TeacherPhoto, Discipline, Review


class InstitutePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutePhoto
        fields = ('photo',)


class ReviewSerializer(serializers.ModelSerializer):
    student = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        write_only=True
    )
    student_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'teacher_id', 'student', 'knowledge_rating', 'teaching_skill_rating', 'easiness_rating',
                  'communication_rating', 'comment', 'created_at', 'is_anonymous', 'student_name')

    def get_student_name(self, obj):
        return obj.student.username


class TeacherPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherPhoto
        fields = '__all__'


class SimpleDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'institute_id', 'logo',)


class InstituteSerializer(serializers.ModelSerializer):
    photos = InstitutePhotoSerializer(many=True, required=False)
    departments = SimpleDepartmentSerializer(many=True, required=False)

    class Meta:
        model = Institute
        fields = ('id', 'name', 'description', 'abbreviation', 'logo', 'photos', 'departments',)


class InstituteWithoutPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ('id', 'name', 'abbreviation', 'logo')


class TeacherCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'institute_id', 'first_photo', 'department_id', 'avg_rating', 'review_count', 'is_published')



class NameDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')


class InstituteDepartmentSerializer(serializers.ModelSerializer):
    departments = NameDepartmentSerializer(many=True, required=False)

    class Meta:
        model = Institute
        fields = ('id', 'name', 'departments')


class DepartmentSerializer(serializers.ModelSerializer):
    teachers = TeacherCardSerializer(many=True, required=False)

    class Meta:
        model = Department
        fields = ('id', 'name', 'description', 'institute_id', 'teachers', 'logo')


class SimpleDisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ('id', 'name',)


class TeacherSerializer(serializers.ModelSerializer):
    photos = TeacherPhotoSerializer(many=True, required=False)
    disciplines = SimpleDisciplineSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)
    created_by = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'department_id', 'alma_mater', 'knowledge_rating', 'teaching_skill_rating', 'easiness_rating',
                  'communication_rating', 'avg_rating', 'institute_id', 'bio', 'photos', 'disciplines', 'reviews',
                  'review_count', 'date_published', 'created_by', 'first_photo')
        read_only_fields = ['knowledge_rating', 'teaching_skill_rating', 'easiness_rating', 'communication_rating',
                            'avg_rating', 'review_count', 'reviews','created_by']


class ModerTeacherSerializer(serializers.ModelSerializer):
    photos = TeacherPhotoSerializer(many=True, required=False)
    disciplines = SimpleDisciplineSerializer(many=True, required=False)

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'department', 'alma_mater', 'institute', 'bio', 'photos', 'disciplines',
                  'date_published', 'created_by', 'is_published',)
        read_only_fields = ['created_by']


class DisciplineSerializer(serializers.ModelSerializer):
    teachers = TeacherCardSerializer(many=True, required=False)

    class Meta:
        model = Discipline
        fields = ('id', 'name', 'teachers')

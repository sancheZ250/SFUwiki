from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Institute, InstitutePhoto, Department, Teacher, TeacherPhoto, Discipline, Review


class InstitutePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutePhoto
        fields = ('photo',)


class ReviewSerializer(serializers.ModelSerializer):
    student = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Review
        fields = ('teacher', 'student', 'knowledge_rating', 'teaching_skill_rating', 'easiness_rating',
                  'communication_rating', 'comment', 'created_at', 'is_anonymous')


class TeacherPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherPhoto
        fields = '__all__'


class InstituteSerializer(serializers.ModelSerializer):
    photos = InstitutePhotoSerializer(many=True, required=False)

    class Meta:
        model = Institute
        fields = ('id', 'name', 'description', 'abbreviation', 'logo', 'photos',)


class InstituteWithoutPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ('id', 'name', 'abbreviation', 'logo')


class TeacherCardSerializer(serializers.ModelSerializer):
    first_photo = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'institute', 'department', 'first_photo', 'avg_rating', 'review_count')

    def get_first_photo(self, obj):
        # Получаем первое фото преподавателя, если оно существует
        first_photo = obj.photos.first()
        if first_photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(first_photo.photo.url)
        return None  # Возвращаем None, если нет фото


class DepartmentSerializer(serializers.ModelSerializer):
    teachers = TeacherCardSerializer(many=True, required=False)

    class Meta:
        model = Department
        fields = ('id', 'name', 'description', 'institute', 'teachers')


class SimpleDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class SimpleDisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ('id', 'name', 'logo')


class TeacherSerializer(serializers.ModelSerializer):
    photos = TeacherPhotoSerializer(many=True, required=False)
    disciplines = SimpleDisciplineSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)
    created_by = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Teacher
        fields = ('name', 'department', 'alma_mater', 'knowledge_rating', 'teaching_skill_rating', 'easiness_rating',
                  'communication_rating', 'avg_rating', 'institute', 'bio', 'photos', 'disciplines', 'reviews',
                  'review_count', 'date_published', 'created_by',)


class ModerTeacherSerializer(serializers.ModelSerializer):
    photos = TeacherPhotoSerializer(many=True, required=False)
    disciplines = SimpleDisciplineSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = Teacher
        fields = ('name', 'department', 'alma_mater', 'knowledge_rating', 'teaching_skill_rating', 'easiness_rating',
                  'communication_rating', 'avg_rating', 'institute', 'bio', 'photos', 'disciplines', 'reviews',
                  'review_count', 'date_published', 'created_by', 'is_published',)


class DisciplineSerializer(serializers.ModelSerializer):
    teachers = TeacherCardSerializer(many=True, required=False)

    class Meta:
        model = Discipline
        fields = ('id', 'name', 'description', 'teachers', 'logo')
from rest_framework import serializers
from .models import Institute, InstitutePhoto, Department, Teacher, TeacherPhoto, Discipline, Review


class InstitutePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutePhoto
        fields = ('photo',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'




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


class TeacherNameAndPhotoSerializer(serializers.ModelSerializer):
    first_photo = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'institute', 'department', 'first_photo', 'knowledge_rating', 'teaching_skill_rating',
                  'easiness_rating', 'communication_rating',)

    def get_first_photo(self, obj):
        # Получаем первое фото преподавателя, если оно существует
        first_photo = obj.photos.first()
        if first_photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(first_photo.photo.url)
        return None  # Возвращаем None, если нет фото


class DepartmentSerializer(serializers.ModelSerializer):
    teachers = TeacherNameAndPhotoSerializer(many=True, required=False)

    class Meta:
        model = Department
        fields = ('id', 'name', 'description', 'institute', 'teachers')

class SimpleDisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ('id', 'name', 'logo')


class TeacherSerializer(serializers.ModelSerializer):
    photos = TeacherPhotoSerializer(many=True, required=False)
    disciplines = SimpleDisciplineSerializer(many=True)
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = Teacher
        fields = ('name', 'department', 'alma_mater', 'knowledge_rating', 'teaching_skill_rating', 'easiness_rating',
                  'communication_rating', 'institute', 'bio', 'photos', 'disciplines', 'reviews',)



class DisciplineSerializer(serializers.ModelSerializer):
    teachers = TeacherNameAndPhotoSerializer(many=True, required=False)
    class Meta:
        model = Discipline
        fields = ('id', 'name', 'description', 'teachers')
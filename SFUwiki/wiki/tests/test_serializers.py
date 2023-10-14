from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from ..models import Institute, InstitutePhoto, Teacher, Department, TeacherPhoto, Discipline, Review
from ..serializers import InstituteSerializer, InstitutePhotoSerializer, DepartmentSerializer, TeacherCardSerializer, \
    TeacherSerializer


class InstituteSerializerTestCase(APITestCase):
    def test_institute_serializer(self):
        # Создание объекта Institute
        institute_data = {
            'name': 'Example Institute',
            'description': 'This is an example institute',
            'abbreviation': 'EI',
        }
        institute = Institute.objects.create(**institute_data)

        photos_data = [{'photo': 'photo1.jpg'}, {'photo': 'photo2.jpg'}]
        for photo_data in photos_data:
            InstitutePhoto.objects.create(institute=institute, **photo_data)

        # Создание сериализатора
        serialized_data = InstituteSerializer(institute).data

        # Проверка, что сериализатор возвращает ожидаемые данные
        self.assertEqual(serialized_data['name'], 'Example Institute')
        self.assertEqual(serialized_data['description'], 'This is an example institute')
        self.assertEqual(serialized_data['abbreviation'], 'EI')
        self.assertEqual(len(serialized_data['photos']), len(photos_data))

    def test_institute_photo_serializer(self):
        # Создание объекта Institute
        institute_data = {
            'name': 'Example Institute',
            'description': 'This is an example institute',
            'abbreviation': 'EI',
        }
        institute = Institute.objects.create(**institute_data)
        photo_data = {'photo': 'sample.jpg', 'institute': institute}
        photo = InstitutePhoto.objects.create(**photo_data)

        serializer = InstitutePhotoSerializer(instance=photo)

        # Проверка, что сериализатор возвращает ожидаемые данные
        self.assertEqual(serializer.data['photo'], '/media/sample.jpg')


class DepartmentSerializerTestCase(APITestCase):
    def test_department_serializer(self):
        institute_data = {
            'name': 'Example Institute',
            'description': 'This is an example institute',
            'abbreviation': 'EI',
        }
        institute = Institute.objects.create(**institute_data)

        department_data = {
            'name': 'Example Department',
            'description': 'This is an example department',
            'institute': institute,
        }
        department = Department.objects.create(**department_data)

        teacher_data = {
            'name': 'John Doe',
            'institute': institute,
            'department': department,
            'knowledge_rating': 5,
            'teaching_skill_rating': 4,
            'easiness_rating': 3,
            'communication_rating': 5,
            'review_count': 10,
        }
        teacher = Teacher.objects.create(**teacher_data)

        # Создайте сериализатор
        serializer = DepartmentSerializer(instance=department)

        # Проверьте, что сериализатор возвращает ожидаемые данные
        self.assertEqual(serializer.data['name'], 'Example Department')
        self.assertEqual(serializer.data['description'], 'This is an example department')
        self.assertEqual(serializer.data['institute'], institute.id)
        self.assertEqual(len(serializer.data['teachers']), 1)


class TeacherSerializerTestCase(APITestCase):
    def test_teacher_card_serializer(self):
        # Создание объекта Institute
        institute_data = {
            'name': 'Example Institute',
            'description': 'This is an example institute',
            'abbreviation': 'EI',
        }
        institute = Institute.objects.create(**institute_data)

        # Создание объекта Department
        department_data = {
            'name': 'Example Department',
            'description': 'This is an example department',
            'institute': institute,
        }
        department = Department.objects.create(**department_data)

        # Создание объекта Teacher
        teacher_data = {
            'name': 'John Doe',
            'institute': institute,
            'department': department,
            'knowledge_rating': 5,
            'teaching_skill_rating': 4,
            'easiness_rating': 3,
            'communication_rating': 5,
            'review_count': 10,
        }
        teacher = Teacher.objects.create(**teacher_data)

        # Создние фото для учителя
        photo_data = {'photo': 'teacher_photo.jpg', 'teacher': teacher}
        TeacherPhoto.objects.create(**photo_data)

        factory = APIRequestFactory()
        request = factory.get('')

        serializer = TeacherCardSerializer(instance=teacher, context={'request': request})

        # Проверка, что сериализатор возвращает ожидаемые данные
        self.assertEqual(serializer.data['name'], 'John Doe')
        self.assertEqual(serializer.data['knowledge_rating'], '5.000')
        self.assertEqual(serializer.data['teaching_skill_rating'], '4.000')
        self.assertEqual(serializer.data['easiness_rating'], '3.000')
        self.assertEqual(serializer.data['communication_rating'], '5.000')
        self.assertEqual(serializer.data['review_count'], 10)
        self.assertTrue('first_photo' in serializer.data)
        self.assertEqual(serializer.data['first_photo'], request.build_absolute_uri('/media/teacher_photo.jpg'))

    def test_teacher_serializer(self):
        # Создание объекта Institute
        institute_data = {
            'name': 'Example Institute',
            'description': 'This is an example institute',
            'abbreviation': 'EI',
        }
        institute = Institute.objects.create(**institute_data)

        # Создайте объект Department
        department_data = {
            'name': 'Example Department',
            'description': 'This is an example department',
            'institute': institute,
        }
        department = Department.objects.create(**department_data)

        # Создание объекта Teacher
        teacher_data = {
            'name': 'John Doe',
            'institute': institute,
            'department': department,
            'knowledge_rating': 5,
            'teaching_skill_rating': 4,
            'easiness_rating': 3,
            'communication_rating': 5,
            'review_count': 10,
            'bio': 'This is John Doe, a great teacher.',
        }
        teacher = Teacher.objects.create(**teacher_data)

        # Создание фото для учителя
        photo_data = {'photo': 'teacher_photo.jpg', 'teacher': teacher}
        TeacherPhoto.objects.create(**photo_data)

        # Создание дисциплины
        discipline_data = {
            'name': 'Math',
            'description': 'math_math_math_math_math',
            'logo': 'logo.jpg'
        }
        Discipline.objects.create(**discipline_data)
        discipline = Discipline.objects.get(name='Math')
        discipline.teachers.add(teacher)
        user_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        user = User.objects.create_user(**user_data)
        # Создание отзыва
        review_data = {
            'teacher': teacher,
            'student': user,
            'knowledge_rating': 5,
            'teaching_skill_rating': 4,
            'easiness_rating': 3,
            'communication_rating': 5,
            'comment': 'John Doe is an amazing teacher!',
            'is_anonymous': False,
        }

        Review.objects.create(**review_data)

        # Создание сериализатора
        serializer = TeacherSerializer(instance=teacher)

        # Проверка, что сериализатор возвращает ожидаемые данные
        self.assertEqual(serializer.data['name'], 'John Doe')
        self.assertEqual(serializer.data['knowledge_rating'], '5.000')
        self.assertEqual(serializer.data['teaching_skill_rating'], '4.000')
        self.assertEqual(serializer.data['easiness_rating'], '3.000')
        self.assertEqual(serializer.data['communication_rating'], '5.000')
        self.assertEqual(serializer.data['review_count'], 10)
        self.assertEqual(serializer.data['bio'], 'This is John Doe, a great teacher.')
        self.assertEqual(serializer.data['disciplines'][0]['logo'], '/media/logo.jpg')
        self.assertTrue('photos' in serializer.data)
        self.assertTrue('disciplines' in serializer.data)
        self.assertTrue('reviews' in serializer.data)

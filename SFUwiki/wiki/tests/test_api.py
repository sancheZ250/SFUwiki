from django.contrib.auth.models import User
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status, serializers
from wiki.serializers import InstituteSerializer, DepartmentSerializer, InstituteWithoutPhotoSerializer, \
    TeacherCardSerializer, SimpleDisciplineSerializer, SimpleDepartmentSerializer, DisciplineSerializer
from wiki.models import Institute, Department, Teacher, TeacherPhoto, Review, Discipline
from django.core.files.uploadedfile import SimpleUploadedFile


class InstituteTestCase(APITestCase):
    def setUp(self):
        self.logo1 = SimpleUploadedFile('logo1.png', b'logo1_content', content_type='image/png')
        self.logo2 = SimpleUploadedFile('logo2.png', b'logo2_content', content_type='image/png')
        # Создаем несколько объектов Institute для тестирования
        self.institute1 = Institute.objects.create(
            name="Institute 1",
            description="Description 1",
            abbreviation="Inst 1",
            logo=self.logo1
        )
        self.institute2 = Institute.objects.create(
            name="Institute 2",
            description="Description 2",
            abbreviation="Inst 2",
            logo=self.logo2
        )

    def test_get_list(self):
        url = reverse('institute-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Проверяем, что получено два объекта Institute
        serializer_data = InstituteWithoutPhotoSerializer([self.institute1, self.institute2], many=True).data
        for inst_data in serializer_data:
            inst_data.pop('logo', None)

        for inst_data in response.data:
            inst_data.pop('logo', None)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('institute-detail', args=[self.institute1.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Institute 1")
        self.assertEqual(response.data['description'], "Description 1")
        self.assertEqual(response.data['abbreviation'], "Inst 1")
        self.assertIsNotNone(response.data['logo'])  # Проверяем, что логотип не None

    def test_create_institute(self):
        url = reverse('institute-list')
        data = {
            'name': 'New Institute',
            'description': 'New Description',
            'abbreviation': 'NA',
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Institute.objects.count(), 3)

        new_institute = Institute.objects.get(name='New Institute')
        self.assertEqual(new_institute.name, 'New Institute')
        self.assertEqual(new_institute.description, 'New Description')
        self.assertEqual(new_institute.abbreviation, 'NA')

    def test_delete_institute(self):
        url = reverse('institute-detail', args=[self.institute1.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Institute.objects.filter(pk=self.institute1.pk).exists())

    def test_update_institute(self):
        url = reverse('institute-detail', args=[self.institute1.pk])
        data = {
            'name': 'Updated Institute Name',
            'description': 'Updated Description',
            'abbreviation': 'UI'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_institute = Institute.objects.get(pk=self.institute1.pk)
        self.assertEqual(updated_institute.name, 'Updated Institute Name')
        self.assertEqual(updated_institute.description, 'Updated Description')
        self.assertEqual(updated_institute.abbreviation, 'UI')


class DepartmentTestCase(APITestCase):
    def setUp(self):
        self.institute = Institute.objects.create(
            name="Test Institute",
            description="Test Description",
            abbreviation="TI",
            logo=None
        )
        self.department1 = Department.objects.create(
            name="Department 1",
            description="Description 1",
            institute=self.institute,
            logo=None
        )
        self.department2 = Department.objects.create(
            name="Department 2",
            description="Description 2",
            institute=self.institute,
            logo=None
        )

    def test_get_list(self):
        url = reverse('institute_departments-list', args=[self.institute.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Проверяем, что получено два объекта Department
        serializer_data = SimpleDepartmentSerializer([self.department1, self.department2], many=True).data
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('institute_departments-detail', args=[self.institute.pk, self.department1.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Department 1")
        self.assertEqual(response.data['description'], "Description 1")
        self.assertEqual(response.data['institute'], self.institute.pk)

    def test_create_department(self):
        url = reverse('institute_departments-list', args=[self.institute.pk])
        data = {
            'name': 'New Department',
            'description': 'New Description',
            'institute': self.institute.pk,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 3)

        new_department = Department.objects.get(name='New Department')
        self.assertEqual(new_department.name, 'New Department')
        self.assertEqual(new_department.description, 'New Description')
        self.assertEqual(new_department.institute.pk, self.institute.pk)

    def test_update_department(self):
        url = reverse('institute_departments-detail', args=[self.institute.pk, self.department1.pk])
        data = {
            'name': 'Update Department',
            'description': 'Update Description',
            'institute': self.institute.pk,
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_department = Department.objects.get(pk=self.department1.pk)
        self.assertEqual(updated_department.name, 'Update Department')
        self.assertEqual(updated_department.description, 'Update Description')
        self.assertEqual(updated_department.institute.pk, self.institute.pk)

    def test_delete_department(self):
        url = reverse('institute_departments-detail', args=[self.institute.pk, self.department1.pk])
        response = self.client.delete(url)


class TeacherTestCase(APITestCase):
    def setUp(self):
        # Создаем институт, отдел и учителя для использования в тестах
        self.institute = Institute.objects.create(
            name="Институт",
            description="Описание института",
            abbreviation="ИНСТ",
        )

        self.department = Department.objects.create(
            name="Кафедра",
            description="Описание кафедры",
            institute=self.institute,
        )

        self.teacher = Teacher.objects.create(
            name="Брежнев Руслан Владимирович",
            department=self.department,
            alma_mater="МГУ",
            bio="Биография учителя",
            knowledge_rating=5.0,
            teaching_skill_rating=5.0,
            easiness_rating=5.0,
            communication_rating=5.0,
            institute=self.institute,
            review_count=0,
        )
        self.teacher2 = Teacher.objects.create(
            name="Другой Учитель",
            department=self.department,
            alma_mater="Другой ВУЗ",
            bio="Биография другого учителя",
            knowledge_rating=4.0,
            teaching_skill_rating=4.0,
            easiness_rating=4.0,
            communication_rating=4.0,
            institute=self.institute,
            review_count=0,
        )
        self.test_photo = SimpleUploadedFile('test.png', b'test_content', content_type='image/png')
        self.test_photo2 = SimpleUploadedFile('test2.png', b'test_content2', content_type='image/png')
        # Создаем объект TeacherPhoto и связываем его с тестовым учителем
        self.teacher_photo = TeacherPhoto.objects.create(
            teacher=self.teacher,
            photo=self.test_photo,
        )
        self.teacher_photo2 = TeacherPhoto.objects.create(
            teacher=self.teacher2,
            photo=self.test_photo,
        )
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.review = Review.objects.create(
            teacher=self.teacher,
            student=self.user,
            knowledge_rating=4,
            teaching_skill_rating=5,
            easiness_rating=3,
            communication_rating=4,
            comment="Отзыв о преподавателе",
            is_anonymous=False
        )
        self.url = reverse('institute_teachers-detail', args=[self.institute.pk, self.teacher.pk])

    def test_get_list(self):
        url = reverse('institute_teachers-list', args=[self.institute.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        # Проверяем, что в ответе API есть фотографии
        for teacher_data, teacher, teacherphoto in zip(response.data, [self.teacher, self.teacher2],
                                                       [self.teacher_photo, self.teacher_photo2]):
            self.assertEqual(teacher_data['first_photo'], f'http://testserver{teacherphoto.photo.url}')
            self.assertEqual(teacher_data['name'], teacher.name)
            self.assertEqual(float(teacher_data['avg_rating'][:-2]), float(teacher.avg_rating))
            self.assertEqual(teacher_data['review_count'], teacher.review_count)

    def test_get_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['name'], self.teacher.name)
        self.assertEqual(response.data['alma_mater'], self.teacher.alma_mater)
        self.assertEqual(response.data['bio'], self.teacher.bio)
        self.assertEqual(response.data['knowledge_rating'][:-2], str(self.teacher.knowledge_rating))
        self.assertEqual(response.data['teaching_skill_rating'][:-2], str(self.teacher.teaching_skill_rating))
        self.assertEqual(response.data['easiness_rating'][:-2], str(self.teacher.easiness_rating))
        self.assertEqual(response.data['communication_rating'][:-2], str(self.teacher.communication_rating))
        self.assertEqual(response.data['review_count'], self.teacher.review_count)

        self.assertIsNotNone(response.data['photos'])
        self.assertEqual(response.data['photos'][0]['photo'], f'http://testserver{self.teacher_photo.photo.url}')

        self.assertIsNotNone(response.data['reviews'])
        self.assertEqual(response.data['reviews'][0]['comment'], self.review.comment)

    def test_create(self):
        data = {
            "name": "Новый Учитель",
            "department": self.department.pk,
            "alma_mater": "Новый ВУЗ",
            "bio": "Биография нового учителя",
            "knowledge_rating": 4.5,
            "teaching_skill_rating": 4.5,
            "easiness_rating": 4.5,
            "communication_rating": 4.5,
            "institute": self.institute.pk,
        }
        response = self.client.post(reverse('institute_teachers-list', args=[self.institute.pk]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверьте, что новый учитель был создан
        self.assertTrue(Teacher.objects.filter(name="Новый Учитель").exists())

    def test_update(self):
        data = {
            "name": "Обновленный Учитель",
            "alma_mater": "Обновленный ВУЗ",
            "bio": "Обновленная биография",
            "knowledge_rating": 4.0,
            "teaching_skill_rating": 4.0,
            "easiness_rating": 4.0,
            "communication_rating": 4.0,
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверьте, что данные учителя были обновлены
        self.teacher.refresh_from_db()
        self.assertEqual(self.teacher.name, "Обновленный Учитель")
        self.assertEqual(self.teacher.alma_mater, "Обновленный ВУЗ")

    def test_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Teacher.objects.filter(pk=self.teacher.id).exists())


def fix_absolute_urls(data):
    base_url = 'http://testserver'
    for item in data:
        item['logo'] = base_url + item['logo']
    return data


class DisciplineTestCase(APITestCase):
    def setUp(self):
        self.institute = Institute.objects.create(
            name="Институт",
            description="Описание института",
            abbreviation="ИНСТ",
        )

        self.department = Department.objects.create(
            name="Кафедра",
            description="Описание кафедры",
            institute=self.institute,
        )

        self.teacher = Teacher.objects.create(
            name="Брежнев Руслан Владимирович",
            department=self.department,
            alma_mater="МГУ",
            bio="Биография преподавателя",
            knowledge_rating=5.0,
            teaching_skill_rating=5.0,
            easiness_rating=5.0,
            communication_rating=5.0,
            institute=self.institute,
            review_count=0,
        )
        self.test_logo1 = SimpleUploadedFile('test.png', b'test_content', content_type='image/png')
        self.test_logo2 = SimpleUploadedFile('test2.png', b'test_content2', content_type='image/png')
        self.discipline1 = Discipline.objects.create(name='Discipline 1', description='Description 1',
                                                     logo=self.test_logo1)
        self.discipline2 = Discipline.objects.create(name='Discipline 2', description='Description 2',
                                                     logo=self.test_logo2)
        self.discipline1.teachers.add(self.teacher)
        self.discipline2.teachers.add(self.teacher)

    def test_get_list(self):
        url = reverse('discipline-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        serialized_data = SimpleDisciplineSerializer([self.discipline1, self.discipline2], many=True).data
        serialized_data = fix_absolute_urls(serialized_data)
        self.assertEqual(serialized_data, response.data)

    def test_get_detail(self):
        url = reverse('discipline-detail', args=[self.discipline1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = DisciplineSerializer(self.discipline1).data
        serialized_data['logo'] = 'http://testserver' + serialized_data['logo']
        self.assertEqual(serialized_data, response.data)

    def test_create_discipline(self):
        url = reverse('discipline-list')

        data = {
            'name': 'New Discipline',
            'description': 'New Description',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Discipline.objects.count(), 3)
        discipline = Discipline.objects.get(name='New Discipline')
        self.assertEqual(discipline.name, 'New Discipline')
        self.assertEqual(discipline.description, 'New Description')

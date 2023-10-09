from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from wiki.serializers import InstituteSerializer, DepartmentSerializer, InstituteWithoutPhotoSerializer
from wiki.models import Institute, Department
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
        serializer_data = DepartmentSerializer([self.department1, self.department2], many=True).data
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('institute_departments-detail', args=[self.institute.pk, self.department1.pk])
        responce = self.client.get(url)

        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.data['name'], "Department 1")
        self.assertEqual(responce.data['description'], "Description 1")
        self.assertEqual(responce.data['institute'], self.institute.pk)

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

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Department.objects.count(), 1)

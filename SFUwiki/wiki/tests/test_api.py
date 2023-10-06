from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from wiki.serializers import InstituteSerializer
from wiki.models import Institute
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
        serializer_data = InstituteSerializer([self.institute1, self.institute2], many=True).data
        for inst_data in serializer_data:
            inst_data.pop('logo', None)

        # Удаляем поле 'logo' из response.data
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

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from wiki.serializers import InstituteSerializer
from wiki.models import Institute


class InstituteTestCase(APITestCase):

    def setUp(self):
        # Создаем несколько объектов Institute для тестирования
        self.institute1 = Institute.objects.create(
            name="Institute 1",
            description="Description 1",
            abbreviation="Inst 1",
            logo=None
        )
        self.institute2 = Institute.objects.create(
            name="Institute 2",
            description="Description 2",
            abbreviation="Inst 2",
            logo=None
        )

    def test_get_list(self):
        url = reverse('institute-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Проверяем, что получено два объекта Institute
        serializer_data = InstituteSerializer([self.institute1, self.institute2], many=True).data
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('institute-detail', args=[self.institute1.pk])  # Замените 'institute-detail' на имя вашего URL-маршрута
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Institute 1")
        self.assertEqual(response.data['description'], "Description 1")
        self.assertEqual(response.data['abbreviation'], "Inst 1")
        self.assertIsNone(response.data['logo'])  # Проверяем, что логотип None (если у вас такая логика)

    # Другие тесты, такие как test_create, test_update, test_delete, можно добавить по аналогии

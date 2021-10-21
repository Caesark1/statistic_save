from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from apps.main.models import Statistic
from apps.main.serializers import StatisticRenderSerializer


class StatisticAPITestCase(APITestCase):

    def test_get(self):
        url = reverse('v1:statistic_list')
        statistic1 = Statistic.objects.create(
            date='2021-10-21'
        )
        statistic2 = Statistic.objects.create(
            date='2021-11-30',
            views=5,
            clicks=5,
            cost=100
        )
        response = self.client.get(url)
        serialized_data = StatisticRenderSerializer((statistic1, statistic2), many=True)
        self.assertEqual(serialized_data.data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_post(self):
        url = reverse('v1:statistic_create')
        response = self.client.post(url, data={'date': '2021-10-15'})
        expected_data = {'date': '2021-10-15', 'views': None, 'clicks': None, 'cost': None}
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_delete(self):
        url = reverse('v1:statistic_destroy')
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

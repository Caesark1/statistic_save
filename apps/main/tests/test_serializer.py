from collections import OrderedDict

from django.test import TestCase

from apps.main.models import Statistic
from apps.main.serializers import StatisticRenderSerializer, StatisticCreateSerializer


class StatisticSerializerTestCase(TestCase):
    def test_first_serializer(self):
        statistic1 = Statistic.objects.create(
            date='2021-10-21'
        )
        statistic2 = Statistic.objects.create(
            date='2021-11-30',
            views=5,
            clicks=5,
            cost=100
        )
        serialized_data = StatisticRenderSerializer((statistic1, statistic2), many=True).data
        expected = [
            OrderedDict(
                [
                    ('date', statistic1.date),
                    ('views', None),
                    ('clicks', None),
                    ('cost', None),
                    ('cpc', None),
                    ('cpm', None)
                ]
            ),
            OrderedDict(
                [
                    ('date', statistic2.date),
                    ('views', 5),
                    ('clicks', 5),
                    ('cost', '100.00'),
                    ('cpc', 20.0),
                    ('cpm', 20000.0)
                ]
            )
        ]
        self.assertEqual(expected, serialized_data)

    def test_second_serializer(self):
        statistic1 = Statistic.objects.create(
            date='2021-10-21'
        )
        statistic2 = Statistic.objects.create(
            date='2021-11-30',
            views=5,
            clicks=5,
            cost=100
        )
        serialized_data = StatisticCreateSerializer((statistic1, statistic2), many=True).data
        expected = [
            OrderedDict(
                [
                    ('date', statistic1.date),
                    ('views', None),
                    ('clicks', None),
                    ('cost', None),
                ]
            ),
            OrderedDict(
                [
                    ('date', statistic2.date),
                    ('views', 5),
                    ('clicks', 5),
                    ('cost', '100.00'),
                ]
            )
        ]
        self.assertEqual(expected, serialized_data)

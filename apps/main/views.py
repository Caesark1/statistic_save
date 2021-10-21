from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from apps.main.serializers import StatisticCreateSerializer, StatisticRenderSerializer
from apps.main.models import Statistic
from apps.main.filter_classes import StatisticFilterSet


class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistic.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_class = StatisticFilterSet

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StatisticCreateSerializer
        return StatisticRenderSerializer

    def destroy(self, request, *args, **kwargs):
        Statistic.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

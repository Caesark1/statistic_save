from rest_framework import serializers

from apps.main.models import Statistic


class StatisticCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ('date', 'views', 'clicks', 'cost')


class StatisticRenderSerializer(serializers.ModelSerializer):
    cpc = serializers.SerializerMethodField()
    cpm = serializers.SerializerMethodField()

    class Meta:
        model = Statistic
        fields = ('date', 'views', 'clicks', 'cost', 'cpc', 'cpm')

    def get_cpc(self, statistic):
        if statistic.cost and statistic.clicks:
            return statistic.cost/statistic.clicks

    def get_cpm(self, statistic):
        if statistic.cost and statistic.views:
            return statistic.cost/statistic.views * 1000

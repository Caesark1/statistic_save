import django_filters

from apps.main.models import Statistic


class StatisticFilterSet(django_filters.FilterSet):
    """
    Statistic Filter to filter statistic with parameters 'date_from' and 'date_to'
    """
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='lte')

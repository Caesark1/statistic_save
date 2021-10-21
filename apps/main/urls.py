from django.urls import path

from apps.main.views import StatisticViewSet

urlpatterns = [
    path('statistics/', StatisticViewSet.as_view({'get': 'list'}), name='statistic_list'),
    path('statistics/create/', StatisticViewSet.as_view({'post': 'create'}), name='statistic_create'),
    path('statistics/delete/', StatisticViewSet.as_view({'delete': 'destroy'}), name='statistic_destroy')
]

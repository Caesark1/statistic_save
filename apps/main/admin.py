from django.contrib import admin

from apps.main.models import Statistic


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('date', 'views', 'clicks', 'cost')
    list_filter = ('date', )

from django.db import models


class Statistic(models.Model):
    """
    Model that stores data about statistics
    """
    date = models.DateField(verbose_name='Дата события')
    views = models.PositiveIntegerField(verbose_name='Количество показов', blank=True, null=True)
    clicks = models.PositiveIntegerField(verbose_name='Количество кликов', blank=True, null=True)
    cost = models.DecimalField(
        verbose_name='Стоимость кликов', blank=True, null=True,
        decimal_places=2, max_digits=10
    )

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистики'

    def __str__(self):
        return f'{self.date}'

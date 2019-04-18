from django.db import models

# Create your models here.


class Route(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


class Station(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    routes = models.ManyToManyField(to=Route, related_name='stations', verbose_name='Маршруты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Остановка'
        verbose_name_plural = 'Остановки'

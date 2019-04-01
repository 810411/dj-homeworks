from django.db import models
# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=32, verbose_name='Производитель')
    additionally = models.TextField(blank=True, verbose_name='Дополнительно')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


class Phone(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, verbose_name='Модель')
    price = models.IntegerField(verbose_name='Стоимость')
    os = models.CharField(max_length=32, verbose_name='Операционая система')
    ram = models.IntegerField(verbose_name='Оперативная память')
    ppi = models.IntegerField(verbose_name='Число пикселей на дюйм')
    double_camera = models.BooleanField(verbose_name='Двойная камера')
    processor = models.CharField(max_length=32, verbose_name='Процессор')
    display = models.CharField(max_length=32, verbose_name='Разрешение экрана')
    radio = models.BooleanField(verbose_name='FM-Радио')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return self.name

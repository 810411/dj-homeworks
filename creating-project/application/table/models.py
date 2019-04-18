from django.db import models

# Create your models here.


class TableField(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя')
    width = models.IntegerField(verbose_name='Ширина', default=1)
    index_number = models.IntegerField(verbose_name='Порядковый номер', unique=True)

    class Meta:
        verbose_name = 'Поле таблицы'
        verbose_name_plural = 'Поля таблицы'

        ordering = ['index_number']

    def __str__(self):
        return self.name


class PathToCsv(models.Model):
    path = models.FilePathField(path='/', match='.+\.csv$', recursive=True)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.pk = 1
        self.path = path
        self.save()

    class Meta:
        verbose_name = 'Путь к CSV'
        verbose_name_plural = 'Путь к CSV'

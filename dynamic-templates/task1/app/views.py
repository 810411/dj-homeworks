import csv

from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста

        with open(settings.INFLATION_CSV, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            tbody = list(reader)

        thead = [value.capitalize() for value in (
            'год', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
            'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', 'всего'
        )]

        context = {
            'thead': thead,
            'tbody': tbody
        }

        return render(request, self.template_name,
                      context)

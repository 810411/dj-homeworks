import csv

from django.shortcuts import render
from django.views import View

from .models import TableField, PathToCsv

csv_filename = 'phones.csv'

pathToCsv = PathToCsv().get_path()

if pathToCsv == '' or pathToCsv != csv_filename:
    PathToCsv().set_path(csv_filename)

else:
    csv_filename = pathToCsv

columns = TableField.objects.values()

if len(columns) == 0:
    TableField.objects.create(name='id', width=1, index_number=1)
    TableField.objects.create(name='name', width=3, index_number=2)
    TableField.objects.create(name='price', width=2, index_number=3)
    TableField.objects.create(name='release_date', width=2, index_number=4)
    TableField.objects.create(name='lte_exists', width=1, index_number=5)

    columns = TableField.objects.values()


class TableView(View):

    def get(self, request):
        with open(csv_filename, 'rt') as csv_file:
            header = []
            table = []
            table_reader = csv.reader(csv_file, delimiter=';')
            for table_row in table_reader:
                if not header:
                    header = {idx: value for idx, value in enumerate(table_row)}
                else:
                    row = {header.get(idx) or 'col{:03d}'.format(idx): value
                           for idx, value in enumerate(table_row)}
                    table.append(row)

            result = render(request, 'table.html', {'columns': columns, 'table': table, 'csv_file': csv_filename})
        return result

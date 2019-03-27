import datetime
import os

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings

FILES_PATH = settings.FILES_PATH


class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:

        file_info_list = []
        parsed_date = None

        for filename in os.listdir(FILES_PATH):
            file_path = os.path.join(FILES_PATH, filename)

            file_info = {
                'name': filename,
                'ctime': datetime.datetime.fromtimestamp(os.stat(file_path).st_ctime),
                'mtime': datetime.datetime.fromtimestamp(os.stat(file_path).st_mtime)
            }
            file_info_list.append(file_info)

        if date:
            date_array = date.split('-')

            try:
                parsed_date = datetime.date(int(date_array[0]), int(date_array[1]), int(date_array[2]))
            except ValueError as e:
                print(f'Wrong url`s parameter value, {e}')

            file_info_list = filter(lambda x: x['ctime'].date() == parsed_date, file_info_list)

        return {
            'files': file_info_list,
            'date': parsed_date
        }


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:

    if name in os.listdir(FILES_PATH):
        file_name = os.path.join(FILES_PATH, name)

        with open(file_name) as f:
            content = f.read()

    else:
        return redirect('file_list')

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

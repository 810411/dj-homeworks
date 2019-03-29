import csv
from urllib.parse import urlencode

from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page = 1

    with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as file:
        station_list = list(csv.DictReader(file))

    paginator = Paginator(station_list, 10)
    request_page = request.GET.get('page')

    if request_page:
        page = int(request_page)

    content = paginator.page(page)

    prev_page_url = content.has_previous() and ('?'.join([reverse(bus_stations),
                                                          urlencode({'page': content.previous_page_number()})]))
    next_page_url = content.has_next() and ('?'.join([reverse(bus_stations),
                                                      urlencode({'page': content.next_page_number()})]))

    return render_to_response('index.html', context={
        'bus_stations': content.object_list,
        'current_page': page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

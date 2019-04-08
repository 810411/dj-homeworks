import time
import random

from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


class TicketPageView(FormMixin, TemplateView):
    form_class = SearchTicket
    template_name = 'app/ticket_page.html'


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    cities = cache.get('cities')
    term = request.GET.get('term')

    if cities is None:
        cities = list(City.objects.all().values_list('name', flat=True))
        cache.set('cities', cities)

    results = list(filter(lambda x: term.lower() in x.lower(), cities))

    return JsonResponse(results, safe=False)

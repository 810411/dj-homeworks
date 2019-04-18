from django.shortcuts import render

from .models import Route

# Create your views here.


def stations_view(request):
    routes = Route.objects.all()

    context = {
        'routes': routes,
        'center': {'y': '55.753595', 'x': '37.621031'},
        'stations': ''
    }

    route = request.GET.get('route')

    if route:
        stations = routes.get(name=route).stations.all()

        context['stations'] = stations

        stations_sort_x = stations.order_by('latitude')
        stations_sort_y = stations.order_by('longitude')

        x_min = stations_sort_x.first().longitude
        x = str(x_min + (stations_sort_x.last().longitude - x_min) / 2)

        y_min = stations_sort_y.first().latitude
        y = str(y_min + (stations_sort_y.last().latitude - y_min) / 2)

        context['center'] = {'y': y, 'x': x}

    return render(request, 'stations.html', context)

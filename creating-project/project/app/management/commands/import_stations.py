import csv

from django.core.management.base import BaseCommand
from app.models import Station, Route


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', 'r') as csvfile:

            reader = csv.DictReader(csvfile, delimiter=';')

            for line in reader:
                station = Station(
                    latitude=line['Latitude_WGS84'],
                    longitude=line['Longitude_WGS84'],
                    name=line['Name']
                )

                station.save()

                route_numbers = [i.strip() for i in line['RouteNumbers'].split(';')]

                for route_number in route_numbers:
                    route = Route.objects.get_or_create(
                        name=route_number
                    )

                    station.routes.add(route[0])
                    station.save()

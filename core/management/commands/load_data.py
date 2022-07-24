from django.core.management.base import BaseCommand
from core.models import Country, City, District

class Command(BaseCommand):
    help = 'Load Countries, Cities and Districts'

    def handle(self, *args, **kwargs):
        Country.objects.all().delete()
        country_names = [
            'Germany', 'Turkey', 'France', 'Spain', 'Italy', 'Serbia', 'Bosnia', 'Norway', 'Poland', 'Hungary', 'Ukraine', 'Russia',
        ]

        if not Country.objects.count():
            for country_name in country_names:
                Country.objects.create(name=country_name)

        # Germany
        germany = Country.objects.get(name='Germany')

        germany_cities = [
            'Berlin',
            'Köln',
            'Hamburg',
            'Düsseldorf', 
            'Leipzig',
            'Stuttgart',
        ]

        for city in germany_cities:
            City.objects.create(name=city, country=germany)

        # Turkey
        turkey = Country.objects.get(name='Turkey')
        turkey_cities = [
            'Ankara',
            'Istanbul',
            'İzmir',
            'Bursa',
            'Adana',
            'Antalya',
            'Rize',
            'Trabzon',
            'Diyarbakır',
            'Kars',
            'Erzurum',
        ]

        for city in turkey_cities:
            City.objects.create(name=city, country=turkey)

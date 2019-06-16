import requests

from django.shortcuts import render

from .models import City
from .forms import CityForm


def _get_city_info(name, country):

    api_id = '4df3accc4d47201443e70388596f3c5c'

    target_url = f'https://api.openweathermap.org/data/2.5/weather?q={name},{country}&units=imperial&appid={api_id}'

    response = requests.get(url=target_url)

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return None


def index(request):

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            if not City.objects.filter(name=form['name'].value(), country=form['country'].value()):
                data = _get_city_info(form['name'].value(), form['country'].value())
                if data:
                    form.save()

    form = CityForm()

    cities = City.objects.all()

    cities_info = []

    for city in cities:

        data = _get_city_info(city.name, city.country)

        if data:
            city_info = {
                'city': data["name"],
                'country': data["sys"]["country"],
                'temp': data["main"]["temp"],
                'pressure': data["main"]["pressure"],
                'humidity': data["main"]["humidity"],
                'icon': data["weather"][0]["icon"]
            }

            cities_info.append(city_info)

    cities_info.reverse()

    context = {'info': cities_info, 'form': form}

    return render(request, 'weather/index.html', context)

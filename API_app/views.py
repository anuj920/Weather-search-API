from django.shortcuts import render
import requests
from django.views.generic import TemplateView
from datetime import datetime
from django.utils.timezone import make_aware


class HomeView(TemplateView):
    template_name = 'form.html'

def city_list(request):
    city_list = {}
    if 'query' in request.GET:
        query = request.GET['query']
        url = 'http://api.openweathermap.org/data/2.5/find?q=%s&units=metric&appid=90bdd6d0fb6e366c2f3e560ca6b4cfcf' % query
        response = requests.get(url)
        city_list = response.json()
    return render(request, 'city.html', {'city_list': city_list,'q':query})

def city_detail(request,pk):
    city_details = {}
    url = 'http://api.openweathermap.org/data/2.5/weather?id=%s&units=metric&APPID=90bdd6d0fb6e366c2f3e560ca6b4cfcf' % pk
    response = requests.get(url)
    city_details = response.json()
    sunrise = city_details['sys']['sunrise']
    sunrise = make_aware(datetime.fromtimestamp(sunrise))
    sunset = city_details['sys']['sunset']
    sunset = make_aware(datetime.fromtimestamp(sunset))
    return render(request,'city_detail.html',{'city_details': city_details,'sr':sunrise,'st':sunset})


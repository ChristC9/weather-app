from django.shortcuts import render

# Create your views here.
import requests
from .models import *
from .forms import CityForm

def index(request):

        url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=04e1009f989244bbd3e499f950663243'
       
        
        city_weather={}
        
        if request.method=='POST':
                form=CityForm(request.POST)
                if form.is_valid():
                        form.save()
        cities=City.objects.all()
        for city in cities:
                response=requests.get(url.format(city)).json()
                city_weather={
                        'city':city.name,
                        'temperature':'{0:.2f}'.format(float(response['main']['temp'])-273.15),
                        'description':response['weather'][0]['description'],
                        'icon':response['weather'][0]['icon']
                }
        form=CityForm()
        return render(request,'weatherapp/index.html',{'weather_data':city_weather,'form':form})


# 'temperature':'{0:.2f}'.format(float(response['main']['temp'])-273.15),
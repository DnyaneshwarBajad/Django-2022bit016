import requests
from django.shortcuts import render
from .forms import CityForm

def get_weather(request):
    weather_data = None
    error = None
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            api_key = "75e3cd1e798d0375b010d3f9da2ba6ca"  # Replace with your actual API key
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": city,
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"],
                }
            else:
                error = "City not found! Please enter a valid city."

    else:
        form = CityForm()

    return render(request, "weather/weather.html", {"form": form, "weather_data": weather_data, "error": error})


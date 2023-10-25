from django.shortcuts import render
import requests
from . import api_key


# Create your views here.
def index(request):
    # if request.method == "POST":

    API_KEY = "16abde96491a8b119dd8d6e3496a4609"

    city = "Bhopal"

    url = "https://api.openweathermap.org/data/2.5/weather"

    api_call = f"{url}?appid={API_KEY}&q={city}"

    response = requests.get(api_call)

    if response.status_code == 200:
        data = response.json()
        print("Data: ", data)
        weather = {
            "city": city,
            "temperature": round(data["main"]["temp"] - 273.15, 2),
            "feels_like": round(data["main"]["feels_like"] - 273.15, 2),
            "description": data["weather"][0]["description"].capitalize(),
            "icon": data["weather"][0]["icon"],
        }
        print(weather)

    else:
        weather = {
            "city": city,
            "temperature": "N/A",
            "feels_like": "N/A",
            "description": "N/A",
            "icon": "N/A",
        }

    context = {"weather": weather}
    # context: a dictionary that allows us to use its values inside of the template

    return render(request, "index.html", context)

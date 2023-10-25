from django.shortcuts import render
import requests
from . import api_key


# Create your views here.
def index(request):
    # if request.method == "POST":

    API_KEY = api_key.API_KEY

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

        # testing getting location from browser

        # HTTP_X_FORWARDED_FOR header is metadata on the incoming request that contains
        # the IP address that the request was originally sent from.

        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]

        else:
            # In case there is no IP address in the HTTP_X_FORWARDED_FOR header,
            # we fall back to using the REMOTE_ADDRESS header instead,
            # which should contain the IP of the most recent proxy that handled the request.
            ip = request.META.get("REMOTE_ADDR")

        print("IP address:", ip)

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

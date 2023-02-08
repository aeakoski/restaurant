import requests
import random

def getRestaurant():
    location = "Drottninggatan 32 Stockholm"
    radius = 1000 # search radius in meters
    types = "Food"

    url = f"https://nominatim.openstreetmap.org/?addressdetails=1&q=Food+near+Drottninggatan+32+Stockholm&format=json&limit=100"

    response = requests.get(url)
    data = response.json()

    restaurants = []
    for result in data:
        lat = result["lat"]
        lon = result["lon"]
        distance = ((float(lat) - 59.333324)**2 + (float(lon) - 18.064167)**2)**0.5 * 111000 # in meters
        if distance <= radius:
            name = result["display_name"]
            address = result["address"]["road"]# + ", " + result["address"]["neighbourhood"] + "," + result["address"]["suburb"]
            restaurants.append({"name": name, "address": address})

    selected_restaurant = random.choice(restaurants)
    print(selected_restaurant["name"])
    return selected_restaurant["name"]


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():

    return render_template('hello.html', name=getRestaurant())

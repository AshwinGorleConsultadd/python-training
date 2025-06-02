import json

with open("./json_utility/weather_data.json", "r") as file:
    data = json.load(file)

locations = data["list"][0]

for item in locations:
    name = item["name"]
    temperature = item["main"]["temp"]
    pressure = item["main"]["pressure"]
    wind_speed = item["wind"]["speed"]
    description = item["weather"][0]["description"]

    print("Location:", name)
    print("Temperature:", temperature)
    print("Pressure:", pressure)
    print("Wind Speed:", wind_speed)
    print("Weather Description:", description)

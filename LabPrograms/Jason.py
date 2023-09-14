import json

filename = input("Enter the JSON filename: ")

with open(filename, 'r') as jFile:
    weatherData = json.load(jFile)

print("Weather Data:")
for entry in weatherData:
    print("City:", entry["city"])
    print("Temperature:", entry["temperature"])
    print("Weather Condition:", entry["weather_condition"])

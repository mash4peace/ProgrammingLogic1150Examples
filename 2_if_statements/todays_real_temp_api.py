"""
The companion to the temperature.py program, but this version
asks weather.gov what today's temperature is, instead of asking the user.
"""


from urllib import request
import json

# A URL which returns the current conditions and forecast for Minneapolis
url = 'https://api.weather.gov/gridpoints/DLH/58,16/forecast'

# Open the URL, and load the response into the program
response = request.urlopen(url).read()
data = json.loads(response)

# Extract the current conditions
current_conditions = data['properties']['periods'][0]

# And read the temperature, and temperature unit
current_temperature = current_conditions['temperature']
temperature_unit = current_conditions['temperatureUnit']

# Here's the current temp
print(f'The current temperature is {current_temperature}{temperature_unit}')

# And finally, an if statement!

if current_temperature < 32:
    print('It is below freezing')
elif current_temperature == 32:
    print('It is freezing')
else:
    print('It is above freezing')


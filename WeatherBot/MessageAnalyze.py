'''
Created on Jan 16, 2019

@author: mingw
'''
import requests
import time

location_name = 'Pittsburgh, PA'
location_coords = {'x': '40.45', 'y': '-79.96'}
request_params = {'token': 'e61b4450fbcc0136c9d45e3bdb947d66'}

while True:
    response_messages = requests.get('https://api.groupme.com/v3/groups/41952934/messages', params = request_params).json()['response']['messages']
    
    for message in response_messages:
        if(message['text'] == 'WeatherBot' or message['text']):
            weather_response = requests.get('https://api.weather.gov/points/' + location_coords['x'] + ',' + location_coords['y'] + '/forecast').json()
            current_weather = weather_response['properties']['periods'][0]['detailedForecast']
            print('Weather for ' + location_name + ': \n' + current_weather)
            request_params['since_id'] = message['id']
    time.sleep(5)
'''
Created on Jan 16, 2019

@author: mingw
'''
import requests
import time

location_name = 'Pittsburgh, PA'
location_coords = {'x': '40.45', 'y': '-79.96'}
request_params = {'token': 'e61b4450fbcc0136c9d45e3bdb947d66'}
<<<<<<< HEAD
#response = requests.get('https://api.groupme.com/v3/groups/YOUR_GROUP_ID/messages', params = request_params)
while True:
    
    response = requests.get('https://api.groupme.com/v3/groups/41952934/messages', params = request_params)
    
    if(response.status_code == 200):
        response_messages = response.json()['response']['messages']
        
        for message in response_messages:
            if(message['text'] == 'Weatherbot' or message['text'] == 'weatherbot' or message['text'] == 'Weatherbot'):
                
                weather_response = requests.get('https://api.weather.gov/points/' + location_coords['x'] + ',' + location_coords['y'] + '/forecast').json()
                current_weather = weather_response['properties']['periods'][0]['detailedForecast']
                to_send = 'Weather for ' + location_name + ': \n' + current_weather
                
                post_params = { 'bot_id': '71907246832da8d8db6f8d8dc5', 'text' : to_send}
                requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
                request_params['since_id'] = message['id']
                break
=======

while True:
    response_messages = requests.get('https://api.groupme.com/v3/groups/41952934/messages', params = request_params).json()['response']['messages']
    
    for message in response_messages:
        if(message['text'] == 'WeatherBot' or message['text']):
            weather_response = requests.get('https://api.weather.gov/points/' + location_coords['x'] + ',' + location_coords['y'] + '/forecast').json()
            current_weather = weather_response['properties']['periods'][0]['detailedForecast']
            print('Weather for ' + location_name + ': \n' + current_weather)
            request_params['since_id'] = message['id']
>>>>>>> 0d8505a6fad64aabbe32b7722ea4b927bec280e1
    time.sleep(5)
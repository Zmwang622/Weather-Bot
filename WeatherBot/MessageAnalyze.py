'''
Created on Jan 16, 2019

@author: mingw
'''
import requests

request_params = {'token': 'e61b4450fbcc0136c9d45e3bdb947d66'}
response_messages = requests.get('https://api.groupme.com/v3/groups/41952934/messages', params = request_params).json()['response']['messages']

for message in response_messages:
    print(message['text'])
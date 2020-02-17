from time import sleep

import requests as rq

URL = 'http://localhost:5000'

def auth(user, pas):
     req = rq.get(URL + '/auth', params={'username': user, 'password': pas})
     print(req.json())
     if req.json()['ok']:
          return req.json()['token']
     else:
          return ''

def my_exit():
     print('Wrong login or password')
     sleep(1)
     exit()

user = input('Your name: ')
pas  = input('Your password: ')

token = auth(user,pas)
if not token:
     my_exit()

print("print your messeges:")
while True:
     req = rq.post(URL + '/send', json={'text': input(), 'token': token})
     if req.json()['ok']:
          print('OK')
     else:
         my_exit()

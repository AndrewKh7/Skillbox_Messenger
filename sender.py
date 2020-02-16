import requests as rq

URL = 'http://localhost:5000'

user = input('Your name:')
print("print your messeges:")
while True:
     print(rq.post(URL + '/send', json={'username': user, 'text': input()}).status_code)

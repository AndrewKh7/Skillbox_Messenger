from time import sleep

import requests as rq
from  datetime import datetime as dt

URL = 'http://localhost:5000'
messeges = []

def get_history_from_server(t=0):
    """
    input:  last messege time
    output: {'messeges':{"username": "str", "text": "str", "time": time } ... }
    """
    # return rq.get(URL + '/history', params={'time': t}).json()['messeges']
    return rq.get(URL + '/history', params={'time': t}).json()['messeges']



def show_messeges(t=0):
    if not messeges:
            return
    for msg in  filter(lambda m: m['time']>t,messeges):
        time = dt.fromtimestamp (msg['time']).strftime(("%d %b %Y %H:%M:%S"))
        print(time, msg['username'],':')
        print(msg['text'])
        print()


def update_chat():
    last_messege_time = 0
    global messeges
    if messeges:
        last_messege_time = float(messeges[-1]['time'])
        messeges.extend(get_history_from_server(last_messege_time))
    else:
        messeges = get_history_from_server()
    if last_messege_time and last_messege_time != messeges[-1]['time']:
        show_messeges(last_messege_time)


def send(user, msg):
    return rq.post(URL + '/send', json={'username': user, 'text': msg}).status_code

def status():
    return rq.get(URL + '/status').json()

def main():
    while True:
        # print(get_history_from_server())
        update_chat()
        sleep(1)

if __name__ == '__main__':
    main()

import time
import random
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
messeges = [
    {
        'username': "Jack",
        'text': "SomeText",
        'time': time.time(),
    },
    {
        'username': "Dan",
        'text': "DenSomeText",
        'time': time.time(),
    },
]

passwords = {
            'Marry': '12345',
            'Sam': '666',
            'Dean': '777',
        }


# Tokens: 'token': {'username': str,'last_active_time': float }
tokens = {}

@app.route('/')
def main():
    return 'Welcome!'


@app.route('/status')
def status():
    return {
        'status': True,
        'time': datetime.now().strftime("%d %b %Y %H:%M:%S"),
    }


@app.route('/send', methods=['POST'])
def send():
    """
    request: {"text": "str", "token": "str"}
    response: {'ok':true}
    """
    data = request.json
    text = data['text']
    token = data['token']
    status = {'ok': True}
    time_moment = time.time()

    if token not in tokens:
        status['ok'] = False
    elif time_moment - tokens[token]['last_active_time'] > 20:
        status['ok'] = False
    else:
        username = tokens[token]['username']
        tokens[token]['last_active_time'] = time_moment
        messeges.append({
            'username': username,
            'text': text,
            'time': time_moment,
        })

    return status


@app.route('/history', methods=['GET'])
def history():
    """
    request: -  last time on client history
    response: {'messeges':{"username": "str", "text": "str", "time": time } ... }
    """
    last_msg_time = float(request.args['time'])
    return {'messeges': list(filter(lambda m: m['time'] > last_msg_time, messeges))}

@app.route('/auth')
def auth():
    user = request.args['username']
    pas = request.args['password']

    if user in passwords and passwords[user] == pas:
        token = str(random.randint(1000000, 9999999))
        tokens[token] = {'username': user, 'last_active_time': time.time()}
        return {
                'ok': True,
                'token': token,
        }
    else:
        return {
                'ok': False,
                'token': '',
        }

app.run()
